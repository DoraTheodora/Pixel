#! /usr/bin/env node
"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var chalk_1 = require("chalk");
var program = require("commander");
var platform_1 = require("../platforms/platform");
var Executor_1 = require("../runner/Executor");
var runDangerSubprocess_1 = require("./utils/runDangerSubprocess");
var sharedDangerfileArgs_1 = require("./utils/sharedDangerfileArgs");
var getRuntimeCISource_1 = require("./utils/getRuntimeCISource");
var inline_1 = require("../runner/runners/inline");
var dslGenerator_1 = require("../runner/dslGenerator");
var debug_1 = require("../debug");
var d = debug_1.debug("process");
var subprocessName;
program
    .usage("[options] <process_name>")
    .description("Does a Danger run, but instead of handling the execution of a Dangerfile it will pass the DSL " +
    "into another process expecting the process to eventually return results back as JSON. If you don't " +
    "provide another process, then it will output to STDOUT.")
    .on("--help", function () {
    console.log("\n");
    console.log("  Docs:");
    console.log("");
    console.log("    -> Danger Process:");
    console.log("       http://danger.systems/js/usage/danger-process.html");
});
sharedDangerfileArgs_1.default(program);
program.action(function (process_name) { return (subprocessName = process_name); }).parse(process.argv);
// The dynamic nature of the program means typecasting a lot
// use this to work with dynamic propeties
var app = program;
if (process.env["DANGER_VERBOSE"] || app.verbose) {
    global.verbose = true;
}
getRuntimeCISource_1.default(app).then(function (source) {
    // This does not set a failing exit code
    if (source && !source.isPR) {
        console.log("Skipping Danger due to this run not executing on a PR.");
    }
    // The optimal path
    if (source && source.isPR) {
        var platform_2 = platform_1.getPlatformForEnv(process.env, source);
        if (!platform_2) {
            console.log(chalk_1.default.red("Could not find a source code hosting platform for " + source.name + "."));
            console.log("Currently Danger JS only supports GitHub and BitBucket Server, if you want other platforms, consider the Ruby version or help out.");
            process.exitCode = 1;
        }
        if (platform_2) {
            var config_1 = {
                stdoutOnly: app.textOnly,
                verbose: app.verbose,
                jsonOnly: false,
                dangerID: app.id || "default",
            };
            d("Config: ", config_1);
            dslGenerator_1.jsonDSLGenerator(platform_2).then(function (dangerJSONDSL) {
                if (!subprocessName) {
                    //  Just pipe it out to the CLI
                    var processInput = runDangerSubprocess_1.prepareDangerDSL(dangerJSONDSL);
                    process.stdout.write(processInput);
                }
                else {
                    d("Sending input To " + subprocessName + ": ", dangerJSONDSL);
                    var exec = new Executor_1.Executor(source, platform_2, inline_1.default, config_1);
                    runDangerSubprocess_1.default([subprocessName], dangerJSONDSL, exec);
                }
            });
        }
    }
});
//# sourceMappingURL=danger-process.js.map