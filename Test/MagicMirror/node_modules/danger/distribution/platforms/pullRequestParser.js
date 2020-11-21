"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var url = require("url");
var includes = require("lodash.includes");
function pullRequestParser(address) {
    var components = url.parse(address, false);
    if (components && components.path) {
        // shape: http://localhost:7990/projects/PROJ/repos/repo/pull-requests/1/overview
        var parts = components.path.match(/(projects\/\w+\/repos\/[\w-]+)\/pull-requests\/(\d+)/);
        if (parts) {
            return {
                repo: parts[1],
                pullRequestNumber: parts[2],
            };
        }
        // shape: http://github.com/proj/repo/pull/1
        if (includes(components.path, "pull")) {
            return {
                repo: components.path.split("/pull")[0].slice(1),
                pullRequestNumber: components.path.split("/pull/")[1],
            };
        }
    }
    return null;
}
exports.pullRequestParser = pullRequestParser;
//# sourceMappingURL=pullRequestParser.js.map