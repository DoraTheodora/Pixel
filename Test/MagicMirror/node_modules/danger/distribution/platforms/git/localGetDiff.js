"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var debug_1 = require("../../debug");
var child_process_1 = require("child_process");
var d = debug_1.debug("localGetDiff");
exports.localGetDiff = function (base, head) {
    return new Promise(function (done) {
        var args = ["diff", base + "..." + head];
        var stdout = "";
        var child = child_process_1.spawn("git", args, { env: process.env });
        d("> git", args.join(" "));
        child.stdout.on("data", function (chunk) {
            stdout += chunk;
        });
        child.stderr.on("data", function (data) {
            console.error("Could not get diff from git between " + base + " and " + head);
            throw new Error(data.toString());
        });
        child.on("close", function (code) {
            if (code === 0) {
                done(stdout);
            }
        });
    });
};
//# sourceMappingURL=localGetDiff.js.map