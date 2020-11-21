"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
var validateDangerfileExists = function (filePath) {
    var stat = null;
    try {
        stat = fs.statSync(filePath);
    }
    catch (error) {
        console.error("Could not find a dangerfile at " + filePath + ", not running against your PR.");
        process.exitCode = 1;
    }
    if (!!stat && !stat.isFile()) {
        console.error("The resource at " + filePath + " appears to not be a file, not running against your PR.");
        process.exitCode = 1;
    }
    return !!stat && stat.isFile();
};
exports.default = validateDangerfileExists;
//# sourceMappingURL=validateDangerfileExists.js.map