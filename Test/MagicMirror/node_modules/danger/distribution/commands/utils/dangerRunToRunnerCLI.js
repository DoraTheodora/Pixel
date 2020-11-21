"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var usesProcessSeparationCommands = ["ci", "pr", "local"];
var dangerRunToRunnerCLI = function (argv) {
    var newCommand = [];
    newCommand.push(argv[0]);
    // e.g. node --inspect distribution/commands/danger-run-ci.js --dangerfile myDangerfile.ts
    // or node distribution/commands/danger-pr.js --dangerfile myDangerfile.ts
    if (argv.length === 1) {
        return ["danger", "runner"];
    }
    else if (argv[0].includes("node")) {
        // convert
        var newJSFile_1 = argv[1];
        usesProcessSeparationCommands.forEach(function (name) {
            newJSFile_1 = newJSFile_1.replace("danger-" + name, "danger-runner");
        });
        newCommand.push(newJSFile_1);
        for (var index = 2; index < argv.length; index++) {
            newCommand.push(argv[index]);
        }
    }
    else {
        // e.g. danger ci --dangerfile
        // if you do `danger run` start looking at args later
        newCommand.push("runner");
        var index = usesProcessSeparationCommands.includes(argv[1]) ? 2 : 1;
        for (; index < argv.length; index++) {
            newCommand.push(argv[index]);
        }
    }
    return newCommand;
};
exports.default = dangerRunToRunnerCLI;
//# sourceMappingURL=dangerRunToRunnerCLI.js.map