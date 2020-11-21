"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs_1 = require("fs");
/**
 * Returns a the typical Dangerfile, depending on it's location
 * taking into account whether it JS or TS by whether those exists.
 *
 * Will throw if it isn't found.
 */
function dangerfilePath(program) {
    if (program.dangerfile) {
        return program.dangerfile;
    }
    if (fs_1.existsSync("dangerfile.ts")) {
        return "dangerfile.ts";
    }
    if (fs_1.existsSync("dangerfile.js")) {
        return "dangerfile.js";
    }
    if (fs_1.existsSync("Dangerfile.ts")) {
        return "Dangerfile.ts";
    }
    if (fs_1.existsSync("Dangerfile.js")) {
        return "Dangerfile.js";
    }
    throw new Error("Could not find a `dangerfile.js` or `dangerfile.ts` in the current working directory.");
}
exports.dangerfilePath = dangerfilePath;
//# sourceMappingURL=file-utils.js.map