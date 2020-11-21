"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var quotes = "```";
exports.default = (function (error) { return "\n## Danger has errored\n\nError: " + error.name + "\n\n" + quotes + "sh\n" + error.stack + "\n" + quotes + "\n\n"; });
//# sourceMappingURL=exceptionRaisedTemplate.js.map