"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
// https://regex101.com/r/dUq4yB/1
var requirePattern = /^.* require\(('|")danger('|")\);?$/gm;
//  https://regex101.com/r/dUq4yB/2
var es6Pattern = /^.* from ('|")danger('|");?$/gm;
/**
 * Updates a Dangerfile to remove the import for Danger
 * @param {string} contents the file path for the dangerfile
 * @returns {string} the revised Dangerfile
 */
exports.default = (function (contents) {
    return contents.replace(es6Pattern, "// Removed import").replace(requirePattern, "// Removed require");
});
//# sourceMappingURL=cleanDangerfile.js.map