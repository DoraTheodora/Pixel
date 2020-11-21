"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var chalk_1 = require("chalk");
process.on("unhandledRejection", function (reason, _p) {
    console.log(chalk_1.default.red("Error: "), reason);
    process.exitCode = 1;
});
exports.default = (function (command) {
    return command
        .option("-v, --verbose", "Verbose output of files")
        .option("-c, --external-ci-provider [modulePath]", "Specify custom CI provider")
        .option("-t, --text-only", "Provide an STDOUT only interface, Danger will not post to your PR")
        .option("-d, --dangerfile [filePath]", "Specify a custom dangerfile path")
        .option("-i, --id [danger_id]", "Specify a unique Danger ID for the Danger run")
        .option("-b, --base [branch_name]", "Base branch");
});
//# sourceMappingURL=sharedDangerfileArgs.js.map