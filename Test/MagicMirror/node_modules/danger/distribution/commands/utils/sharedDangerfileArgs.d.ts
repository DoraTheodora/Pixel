import * as program from "commander";
export interface SharedCLI extends program.CommanderStatic {
    verbose: boolean;
    externalCiProvider: string;
    textOnly: boolean;
    dangerfile: string;
    id: string;
    repl: string;
}
declare const _default: (command: any) => any;
export default _default;
