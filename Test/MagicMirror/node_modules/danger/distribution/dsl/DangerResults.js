"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var Violation_1 = require("../dsl/Violation");
/// End of Danger DSL definition
exports.emptyDangerResults = {
    fails: [],
    warnings: [],
    messages: [],
    markdowns: [],
};
function validateResults(results) {
    // The data we get back is JSON sent by STDIN that can come from many
    // consumers, let's take the time to ensure the data is how we think it is.
    var fails = results.fails, warnings = results.warnings, messages = results.messages, markdowns = results.markdowns;
    var props = { fails: fails, warnings: warnings, messages: messages, markdowns: markdowns };
    Object.keys(props).forEach(function (name) {
        //
        // Must include the key 4 types
        if (!props[name]) {
            throw new Error("Results passed to Danger JS did not include " + name + ".\n\n" + JSON.stringify(results, null, "  "));
        }
        var violations = props[name];
        violations.forEach(function (v) {
            // They should always have a message
            if (!v.message) {
                throw new Error("A violation passed to Danger JS in " + name + " did not include `message`.\n\n" + JSON.stringify(v, null, "  "));
            }
            // Warn if anything other than the initial API is on a violation
            var officialAPI = ["message", "line", "file"];
            var keys = Object.keys(v).filter(function (f) { return !officialAPI.includes(f); });
            if (keys.length) {
                console.warn("Received unexpected key in Violation, expected only " + officialAPI + " but got " + Object.keys(v));
            }
        });
    });
}
exports.validateResults = validateResults;
/** Returns only the inline violations from Danger results */
function inlineResults(results) {
    return {
        fails: results.fails.filter(function (m) { return Violation_1.isInline(m); }),
        warnings: results.warnings.filter(function (m) { return Violation_1.isInline(m); }),
        messages: results.messages.filter(function (m) { return Violation_1.isInline(m); }),
        markdowns: results.markdowns.filter(function (m) { return Violation_1.isInline(m); }),
    };
}
exports.inlineResults = inlineResults;
/** Returns only the main-comment comments violations from Danger results */
function regularResults(results) {
    return {
        fails: results.fails.filter(function (m) { return !Violation_1.isInline(m); }),
        warnings: results.warnings.filter(function (m) { return !Violation_1.isInline(m); }),
        messages: results.messages.filter(function (m) { return !Violation_1.isInline(m); }),
        markdowns: results.markdowns.filter(function (m) { return !Violation_1.isInline(m); }),
    };
}
exports.regularResults = regularResults;
/** Concat all the violations into a new results */
function mergeResults(results1, results2) {
    return {
        fails: results1.fails.concat(results2.fails),
        warnings: results1.warnings.concat(results2.warnings),
        messages: results1.messages.concat(results2.messages),
        markdowns: results1.markdowns.concat(results2.markdowns),
    };
}
exports.mergeResults = mergeResults;
/** Sorts all of the results according to their files and lines */
function sortInlineResults(inlineResults) {
    // First sort messages in every inline result
    var sortedInlineResults = inlineResults.map(function (i) {
        return {
            file: i.file,
            line: i.line,
            fails: i.fails.sort(),
            warnings: i.warnings.sort(),
            messages: i.messages.sort(),
            markdowns: i.markdowns.sort(),
        };
    });
    // Then sort a whole array of inline results based on file/line
    return sortedInlineResults.sort(function (a, b) {
        if (a.file < b.file) {
            return -1;
        }
        else if (a.file > b.file) {
            return 1;
        }
        else if (a.line < b.line) {
            return -1;
        }
        else if (a.line > b.line) {
            return 1;
        }
        else {
            // both file & line are the same
            return 0;
        }
    });
}
exports.sortInlineResults = sortInlineResults;
function sortResults(results) {
    var sortByFile = function (a, b) {
        if (a.file === undefined) {
            return -1;
        }
        if (b.file === undefined) {
            return 1;
        }
        if (a.file == b.file) {
            if (a.line == undefined) {
                return -1;
            }
            if (b.line == undefined) {
                return 1;
            }
            if (a.line < b.line) {
                return -1;
            }
            else if (a.line > b.line) {
                return 1;
            }
            else {
                return 0;
            }
        }
        if (a.file < b.file) {
            return -1;
        }
        else {
            return 1;
        }
    };
    return {
        fails: results.fails.sort(sortByFile),
        warnings: results.warnings.sort(sortByFile),
        messages: results.messages.sort(sortByFile),
        markdowns: results.markdowns.sort(sortByFile),
    };
}
exports.sortResults = sortResults;
exports.emptyResults = function () { return ({ fails: [], markdowns: [], warnings: [], messages: [] }); };
exports.isEmptyResults = function (results) {
    return results.fails.concat(results.warnings, results.messages, results.markdowns).length === 0;
};
exports.isMarkdownOnlyResults = function (results) {
    return results.markdowns.length > 0 && results.fails.concat(results.warnings, results.messages).length === 0;
};
function resultsIntoInlineResults(results) {
    // Here we iterate through all keys ("fails", "warnings", "messages", "markdowns") and for each violation
    // in given kind we produce new DangerInlineResult or append a violation to existing result. This is all
    // happening in a `violationsIntoInlineResults` function that mutates an out-of-scope variable `dangerInlineResults`.
    var dangerInlineResults = [];
    var violationsIntoInlineResults = function (kind) {
        var _loop_1 = function (violation) {
            if (violation.file && violation.line) {
                var findInlineResult = dangerInlineResults.find(function (r) { return r.file == violation.file && r.line == violation.line; });
                if (findInlineResult) {
                    findInlineResult[kind].push(violation.message);
                }
                else {
                    var inlineResult = {
                        file: violation.file,
                        line: violation.line,
                        fails: [],
                        warnings: [],
                        messages: [],
                        markdowns: [],
                    };
                    inlineResult[kind].push(violation.message);
                    dangerInlineResults.push(inlineResult);
                }
            }
        };
        for (var _i = 0, _a = results[kind]; _i < _a.length; _i++) {
            var violation = _a[_i];
            _loop_1(violation);
        }
    };
    Object.keys(results).forEach(violationsIntoInlineResults);
    return dangerInlineResults;
}
exports.resultsIntoInlineResults = resultsIntoInlineResults;
function inlineResultsIntoResults(inlineResults) {
    var messageToViolation = function (message) {
        return { message: message, file: inlineResults.file, line: inlineResults.line };
    };
    return {
        fails: inlineResults.fails.map(messageToViolation),
        warnings: inlineResults.warnings.map(messageToViolation),
        messages: inlineResults.messages.map(messageToViolation),
        markdowns: inlineResults.markdowns.map(messageToViolation),
    };
}
exports.inlineResultsIntoResults = inlineResultsIntoResults;
//# sourceMappingURL=DangerResults.js.map