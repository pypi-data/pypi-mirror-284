import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { ISettingRegistry } from '@jupyterlab/settingregistry';
import { INotebookTracker, NotebookActions } from '@jupyterlab/notebook';
import { ToolbarButton } from '@jupyterlab/apputils'; 

// Creates a new cell and fills it with the string contents
function createNewCell(notebookTracker: INotebookTracker, contents: string) {
  const current = notebookTracker.currentWidget;
  const notebook = current?.content;

  if (notebook != null) {
    NotebookActions.insertBelow(notebook);
    const activeCell = notebook.activeCell;

    if (activeCell != null) {
      activeCell.model.sharedModel.setSource(contents);
    }
  }
}

// Selects the active cell in the notebook and moves the cursor to the specified line and character
function setCursorPosition(notebookTracker: INotebookTracker, line: number, character: number = 0) {
  const notebookPanel = notebookTracker.currentWidget;
  if (notebookPanel && notebookPanel.content.widgets.length > 0) {
    const notebook = notebookPanel.content;
    const lastCell = notebook.activeCell;

    notebook.activate(); // Ensure the notebook is focused and active

    if (lastCell && lastCell.editor) {
      lastCell.editor.focus();
      lastCell.editor.setCursorPosition({ line: line, column: character });
    } else {
      console.error('Cell editor is null');
    }
  }
}

// sleeps for a specified period of time using a promise and timeout
async function sleep(ms: number) {
  await new Promise(resolve => setTimeout(resolve, ms));
}

const extensionID = '@jaredstef/headers';

const plugin: JupyterFrontEndPlugin<void> = {
  id: `${extensionID}:plugin`,
  description: 'A JupyterLab extension.',
  autoStart: true,
  requires: [INotebookTracker], // Add INotebookTracker to the requires array
  optional: [ISettingRegistry],
  activate: async (app: JupyterFrontEnd, notebookTracker: INotebookTracker, settingRegistry: ISettingRegistry | null) => {
    console.log('JupyterLab extension headers is activated!');

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

    // Run for each newly opened notebook
    notebookTracker.widgetAdded.connect((_, notebookPanel) => {

      // Create buttons if enabled 
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

      // Create custom buttons if enabled 
      if (customButtons && customButtonsEnabled) {
        customButtons.forEach((button, index) => {
          const custom_cell_command = `${extensionID}:createCustomCell${index}`;

          // Register Command
          app.commands.addCommand(custom_cell_command, {
            label: `Insert Custom Cell ${index}`,
            execute: async () => {        
              createNewCell(notebookTracker, button.contentString.replace(/\\n/g, '\n'));
              await sleep(sleep_time);
              setCursorPosition(notebookTracker, button.lineNumber-1, button.characterNumber);
            }
          });

          const customButton = new ToolbarButton({
            label: button.title,
            className: 'button-style',
            onClick: async () => {
              app.commands.execute(custom_cell_command);
            },
            tooltip: `Create custom cell: ${button.title}`
          });
      
          notebookPanel.toolbar.insertItem(4 + index, `customButton${index}`, customButton);
        });
      }

    });

    // Register Commands and Keybindings
    if (sparkButtonEnabled) {
      app.commands.addCommand(spark_cell_command, {
        label: 'Insert Spark Cell',
        execute: async () => {        
            createNewCell(notebookTracker, "%%spark\n\n");
            await sleep(sleep_time);
            setCursorPosition(notebookTracker, 2);
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
            setCursorPosition(notebookTracker, 0, 1);
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
          setCursorPosition(notebookTracker, 0, 1);
      }
    });
  }
};

export default plugin;