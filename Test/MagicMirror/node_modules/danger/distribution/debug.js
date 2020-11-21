"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var debugModule = require("debug");
exports.debug = function (value) {
    var d = debugModule("danger:" + value);
    // In Peril, when running inside Hyper, we don't get access to stderr
    // so bind debug to use stdout
    if (process.env.x_hyper_content_sha256) {
        d.log = console.log.bind(console);
    }
    return d;
};
//# sourceMappingURL=debug.js.map