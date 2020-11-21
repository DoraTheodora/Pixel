#! /usr/bin/env node
"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var program = require("commander");
var sharedDangerfileArgs_1 = require("./utils/sharedDangerfileArgs");
var runner_1 = require("./ci/runner");
program.usage("[options]").description("Reset the status of a GitHub PR to pending.");
sharedDangerfileArgs_1.default(program).parse(process.argv);
var app = program;
runner_1.runRunner(app);
//# sourceMappingURL=danger-reset-status.js.map