import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { IMainMenu } from '@jupyterlab/mainmenu';
//import { ICommandPalette } from '@jupyterlab/apputils';
import { MenuSvg } from '@jupyterlab/ui-components';
import { //INotebookModel,
    INotebookTools,
    INotebookTracker,
    NotebookActions
    } from '@jupyterlab/notebook';
import { Cell } from '@jupyterlab/cells';

/**
 * Utility functions
 */

//Debug status
const debug:boolean = true;

/**
 * Initialization data for the jupyterpidaq-menu extension.
 */

// Useful structure for defining commands to reuse info in menus and commandRegistry
interface CmdandInfo {
 id: string;
 label: string;
 caption: string;
}

const plugin: JupyterFrontEndPlugin<void> = {
    id: 'jupyterpidaq-menu:plugin',
    description: 'Convenience menu for JupyterPiDAQ that runs in Jupyter Lab and Notebook >=7.',
    autoStart: true,
    requires: [IMainMenu, INotebookTracker, INotebookTools],
    activate: (app: JupyterFrontEnd,
          MainMenu: IMainMenu,
          notebookTracker: INotebookTracker,
          notebookTools: INotebookTools
    ) => {
        const { commands } = app;
        /**
         * Utility functions
         */
        function replaceCellContents(cell:Cell, content:string){
            const cellEditor = cell.editor;
            if (cellEditor) {
                const startPos = {column:0, line:0};
                const endline = cellEditor.lineCount - 1;
                let endPos = {column:0, line:endline};
                const endlinecont = cellEditor.getLine(endline);
                if (endlinecont){
                    endPos.column = endlinecont.length;
                    }
                cellEditor.setSelection({start:startPos, end: endPos});
                if (cellEditor.replaceSelection){
                    cellEditor.replaceSelection(content);
                }
            }
        }

        async function insertnewcellwithcontent(content:string){
            const currentnotebook = notebookTracker.currentWidget;
            if (currentnotebook){
                const notebookcontent = currentnotebook.content;
                if (notebookcontent){
                    const selectedcellindex = notebookcontent.activeCellIndex;
                    await NotebookActions.insertBelow(notebookcontent);
                    notebookcontent.activeCellIndex = selectedcellindex +1;
                    const cell = notebookTools.activeCell;
                    if (cell){
                        await cell.ready;
                        if (debug) {
                            console.log('selected cell index:'+selectedcellindex);
                            console.log('index set to:'+notebookcontent.activeCellIndex);
                            console.log('cell:', cell);
                        }
                        replaceCellContents(cell, content);}
                } else {
                    if (debug){
                        console.log('No cell found at index to insert into.');
                    }
                }
            }
        }

        /**
         * Build the commands to add to the menu
         */
        const InsertNewRun:CmdandInfo = {
            id: 'InsertNewRun:jupyterpidaq-menu:mainmenu',
            label: 'Insert new run after selected cell',
            caption: 'Create a new cell and insert skeleton code to create a new run.'
        };
        commands.addCommand(InsertNewRun.id,{
            label: InsertNewRun.label,
            caption: InsertNewRun.caption,
            execute: async () => {
                let pythonstr = '# Insert the name you want for the run (eg. Trial_1).\n';
                pythonstr += '# Then execute this cell to setup and start data collection.\n';
                pythonstr += 'Run("REPLACE_WITH_DESCRIPTIVE_RUN_NAME")';
                insertnewcellwithcontent(pythonstr);
                if (debug){console.log('Inserted New Run Code Cell.');}
            }
        });

        const ShowDataInTable:CmdandInfo = {
            id: 'ShowDataInTable:jupyterpidaq-menu:mainmenu',
            label: 'Select data to show in a table...',
            caption: 'Create a new cell and GUI to select data to display in table.'
        };
        commands.addCommand(ShowDataInTable.id,{
            label: ShowDataInTable.label,
            caption: ShowDataInTable.caption,
            execute: async () => {
                let pythonstr = 'showDataTable()';
                await insertnewcellwithcontent(pythonstr);
                commands.execute('notebook:run-cell');
                if (debug){console.log('ShowData Cell run.');}
            }
        });

        const newCalculatedColumn:CmdandInfo = {
            id: 'newCalculatedColumn:jupyterpidaq-menu:mainmenu',
            label: 'Calculate new column...',
            caption: 'Create a new cell and GUI to calculate a new column.'
        };
        commands.addCommand(newCalculatedColumn.id,{
            label: newCalculatedColumn.label,
            caption: newCalculatedColumn.caption,
            execute: async () => {
                let pythonstr = 'newCalculatedColumn()';
                await insertnewcellwithcontent(pythonstr);
                commands.execute('notebook:run-cell');
                if (debug){console.log('newCalculatedColumn Cell run.');}
            }
        });

        const newPlot:CmdandInfo = {
            id: 'newPlot:jupyterpidaq-menu:mainmenu',
            label: 'Insert new plot after selected cell',
            caption: 'Create a new cell and GUI to create a new plot.'
        };
        commands.addCommand(newPlot.id,{
            label: newPlot.label,
            caption: newPlot.caption,
            execute: async () => {
                let pythonstr = 'newPlot()';
                await insertnewcellwithcontent(pythonstr);
                commands.execute('notebook:run-cell');
                if (debug){console.log('newPlot Cell run.');}
            }
        });

        const newFit:CmdandInfo = {
            id: 'newFit:jupyterpidaq-menu:mainmenu',
            label: 'Insert new fit after selected cell',
            caption: 'Create a new cell and GUI to create a new fit.'
        };
        commands.addCommand(newFit.id,{
            label: newFit.label,
            caption: newFit.caption,
            execute: async () => {
                let pythonstr = 'newFit()';
                await insertnewcellwithcontent(pythonstr);
                commands.execute('notebook:run-cell');
                if (debug){console.log('newPlot Cell run.');}
            }
        });

        /**
        * Create the menu that exposes these commands.
        */
        const menu = new MenuSvg({ commands });
        menu.title.label = 'DAQ Commands';
        menu.addClass('jp-jupyterpidaq-menu');
        menu.addItem({
            command: InsertNewRun.id,
            args: {label:InsertNewRun.label, caption: InsertNewRun.caption}
        });
        menu.addItem({
            command: ShowDataInTable.id,
            args: {label:ShowDataInTable.label, caption: ShowDataInTable.caption}
        });
        menu.addItem({
            command: newCalculatedColumn.id,
            args: {label:newCalculatedColumn.label, caption: newCalculatedColumn.caption}
        });
        menu.addItem({
            command: newPlot.id,
            args: {label:newPlot.label, caption: newPlot.caption}
        });
        menu.addItem({
            command: newFit.id,
            args: {label:newFit.label, caption: newFit.caption}
        });
        MainMenu.addMenu(menu);
        if(debug){console.log('DAQ Commands menu creation complete.');}
        console.log('JupyterLab extension jupyterpidaq-menu is activated!');
    }
};

export default plugin;
