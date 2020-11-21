"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.markdownCode = function (string) { return "\n```sh\n" + string + "\n```\n"; };
exports.resultsWithFailure = function (failure, moreMarkdown) {
    var fail = { message: failure };
    return {
        warnings: [],
        messages: [],
        fails: [fail],
        markdowns: moreMarkdown ? [{ message: moreMarkdown }] : [],
    };
};
exports.mergeResults = function (left, right) {
    return {
        warnings: left.warnings.concat(right.warnings),
        messages: left.messages.concat(right.messages),
        fails: left.fails.concat(right.fails),
        markdowns: left.markdowns.concat(right.markdowns),
    };
};
//# sourceMappingURL=reporting.js.map