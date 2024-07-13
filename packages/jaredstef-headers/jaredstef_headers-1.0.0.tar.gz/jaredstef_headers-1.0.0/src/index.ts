import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { ISettingRegistry } from '@jupyterlab/settingregistry';
import { INotebookTracker, NotebookActions } from '@jupyterlab/notebook'; // Import INotebookTracker
import { ToolbarButton } from '@jupyterlab/apputils'; // Import ToolbarButton

/**
 * Initialization data for the header extension.
 */

const createNewCell = function(notebookTracker: INotebookTracker, contents: string) {
  console.log('called');
  const current = notebookTracker.currentWidget;
          const notebook = current?.content;
          
          if (notebook != null) {
            NotebookActions.insertBelow(notebook);
            const activeCell = notebook.activeCell;
          
            if (activeCell != null) {
              activeCell.model.sharedModel.setSource(contents);
            }
          }
};

const selectLastCell = function(notebookTracker: INotebookTracker, line: number, character: number = 0) {
  const notebookPanel = notebookTracker.currentWidget;
  if (notebookPanel && notebookPanel.content.widgets.length > 0) {
    const notebook = notebookPanel.content;
    // const lastCellIndex = notebook.widgets.length - 1;
    const lastCell = notebook.activeCell;//widgets[lastCellIndex];

    notebook.activate(); // Ensure the notebook is focused and active
    // Select and activate the last cell
    // notebook.activeCellIndex = lastCell.; // This selects and activates the cell

    // Check if the editor of the last cell is instantiated
    if (lastCell && lastCell.editor) {
      lastCell.editor.focus(); // Focus the editor of the last cell
      lastCell.editor.setCursorPosition({ line: line, column: character }); // Example position
    } else {
      console.error('Cell editor is null');
    }
  }
}

async function sleep(ms: number) {
  await new Promise(resolve => setTimeout(resolve, ms));
}

const extensionID = 'headers';

const plugin: JupyterFrontEndPlugin<void> = {
  id: `${extensionID}:plugin`,
  description: 'A JupyterLab extension.',
  autoStart: true,
  requires: [INotebookTracker], // Add INotebookTracker to the requires array
  optional: [ISettingRegistry],
  activate: async (app: JupyterFrontEnd, notebookTracker: INotebookTracker, settingRegistry: ISettingRegistry | null) => {
    console.log('JupyterLab extension headers is activated!');
  
    const spark_cell_command = `${extensionID}:createSparkCell`;
    const exclam_cell_command = `${extensionID}:createExclamCell`;
    const perc_cell_command = `${extensionID}:createHashCell`;

    const sleep_time = 1; 

    const settings = await settingRegistry?.load(plugin.id);

    const sparkButtonEnabled = settings?.get('sparkButtonEnabled').composite;
    const exclamButtonEnabled = settings?.get('exclamButtonEnabled').composite;
    const percButtonEnabled = settings?.get('percButtonEnabled').composite;
    const customButtonsEnabled = settings?.get('customButtonsEnabled').composite;

    const customButtons = settings?.get('customButtons').composite as Array<{
      title: string;
      contentString: string;
      lineNumber: number;
      characterNumber: number;
    }>;

    // Add a toolbar button to each newly opened notebook
    notebookTracker.widgetAdded.connect((sender, notebookPanel) => {

      if (sparkButtonEnabled) {
        const sparkButton = new ToolbarButton({
          label: 'Spark',
          className: 'button-style',
          onClick: async () => {
            
            app.commands.execute(spark_cell_command);
          },
          tooltip: 'Create Spark Magic Cell (@)'
        });
    
        notebookPanel.toolbar.insertItem(1, 'sparkButton', sparkButton);
      }

      if (exclamButtonEnabled) {

        const exclamButton = new ToolbarButton({
          label: '!',
          className: 'button-style',
          onClick: async () => {
            app.commands.execute(exclam_cell_command);
          },
          tooltip: 'Create IPython ! Cell (!)'
        });
    
        notebookPanel.toolbar.insertItem(2, '!Button', exclamButton);
      }

      if (percButtonEnabled) {
        const percentButton = new ToolbarButton({
          label: '%',
          className: 'button-style',
          onClick: async () => {
            app.commands.execute(perc_cell_command);
          },
          tooltip: 'Create IPython % Cell (Shift F5)'
        });
    
        notebookPanel.toolbar.insertItem(3, '%Button', percentButton);
      }

      if (customButtons && customButtonsEnabled) {
        customButtons.forEach((button, index) => {
          const customButton = new ToolbarButton({
            label: button.title,
            className: 'button-style',
            onClick: async () => {
              createNewCell(notebookTracker, button.contentString.replace(/\\n/g, '\n'));
              await sleep(sleep_time);
              selectLastCell(notebookTracker, button.lineNumber-1, button.characterNumber-1);
            },
            tooltip: `Create custom cell: ${button.title}`
          });
      
          notebookPanel.toolbar.insertItem(4 + index, `customButton${index}`, customButton);
        });
      }

    });


    if (sparkButtonEnabled) {
      app.commands.addCommand(spark_cell_command, {
        label: 'Insert Spark Cell',
        execute: async () => {        
            createNewCell(notebookTracker, "%%spark\n\n");
            await sleep(sleep_time);
            selectLastCell(notebookTracker, 2);
        }
      });

      app.commands.addKeyBinding({
        command: spark_cell_command,
        keys: ['Accel Shift 2'],
        selector: '.jp-Notebook'
      });
  
      app.commands.addKeyBinding({
        command: spark_cell_command,
        keys: ['Shift 2'],
        selector: '.jp-Notebook.jp-mod-commandMode'
      });
    }

    if(exclamButtonEnabled) {
      app.commands.addKeyBinding({
        command: exclam_cell_command,
        keys: ['Accel Shift 1'],
        selector: '.jp-Notebook'
      });
  
      app.commands.addKeyBinding({
        command: exclam_cell_command,
        keys: ['Shift 1'],
        selector: '.jp-Notebook.jp-mod-commandMode'
      });

      app.commands.addCommand(exclam_cell_command, {
        label: 'Insert IPython ! Cell',
        execute: async () => {
            createNewCell(notebookTracker, "!");
            await sleep(sleep_time);
            selectLastCell(notebookTracker, 0, 1);
        }
      });
    }

    if (percButtonEnabled) {

      app.commands.addKeyBinding({
        command: perc_cell_command,
        keys: ['Accel Shift F5'],
        selector: '.jp-Notebook'
      });
  
      app.commands.addKeyBinding({
        command: perc_cell_command,
        keys: ['Shift F5'],
        selector: '.jp-Notebook.jp-mod-commandMode'
      });
    }
    


    app.commands.addCommand(perc_cell_command, {
      label: 'Insert IPython % Cell',
      execute: async () => {
          createNewCell(notebookTracker, "%");
          await sleep(sleep_time);
          selectLastCell(notebookTracker, 0, 1);
      }
    });

    if (settingRegistry) {
      settingRegistry
        .load(plugin.id)
        .then(settings => {
          console.log('headers settings loaded:', settings.composite);
        })
        .catch(reason => {
          console.error('Failed to load settings for headers.', reason);
        });
    }
  }
};

export default plugin;