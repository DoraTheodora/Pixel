"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : new P(function (resolve) { resolve(result.value); }).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (_) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
var _this = this;
Object.defineProperty(exports, "__esModule", { value: true });
var DangerResults_1 = require("../../../../dsl/DangerResults");
var githubIssueTemplate_1 = require("../../../../runner/templates/githubIssueTemplate");
var debug_1 = require("../../../../debug");
var d = debug_1.debug("GitHub::ResultsToCheck");
exports.resultsToCheck = function (results, options, pr, api) { return __awaiter(_this, void 0, void 0, function () {
    var repo, hasFails, hasWarnings, mainResults, annotationResults, mainBody, getBlobUrlForPath, annotations, isEmpty;
    var _this = this;
    return __generator(this, function (_a) {
        switch (_a.label) {
            case 0:
                repo = pr.base.repo;
                hasFails = results.fails.length > 0;
                hasWarnings = results.warnings.length > 0;
                mainResults = DangerResults_1.regularResults(results);
                annotationResults = DangerResults_1.inlineResults(results);
                mainBody = githubIssueTemplate_1.template(options.dangerID, mainResults);
                getBlobUrlForPath = function (path) { return __awaiter(_this, void 0, void 0, function () {
                    var data, error_1;
                    return __generator(this, function (_a) {
                        switch (_a.label) {
                            case 0:
                                _a.trys.push([0, 2, , 3]);
                                return [4 /*yield*/, api.repos.getContent({ repo: pr.head.repo.name, owner: pr.head.repo.owner.login, path: path })];
                            case 1:
                                data = (_a.sent()).data;
                                d("Got content data for: ", path);
                                // https://developer.github.com/v3/checks/runs/#example-of-completed-conclusion
                                // e.g.  "blob_href": "http://github.com/octocat/Hello-World/blob/837db83be4137ca555d9a5598d0a1ea2987ecfee/README.md",
                                return [2 /*return*/, pr.head.repo.html_url + "/blob/" + data.sha + "/" + data.path];
                            case 2:
                                error_1 = _a.sent();
                                console.error("An error was raised in getting the blob path for " + path + " - " + error_1);
                                return [2 /*return*/, ""];
                            case 3: return [2 /*return*/];
                        }
                    });
                }); };
                d("Generating inline annotations");
                return [4 /*yield*/, inlineResultsToAnnotations(annotationResults, options, getBlobUrlForPath)];
            case 1:
                annotations = _a.sent();
                isEmpty = !results.fails.length && !results.markdowns.length && !results.warnings.length && !results.messages.length;
                return [2 /*return*/, {
                        name: "Danger",
                        status: "completed",
                        completed_at: new Date().toISOString(),
                        // Repo Metadata
                        owner: repo.owner.login,
                        repo: repo.name,
                        head_branch: pr.head.ref,
                        head_sha: pr.head.sha,
                        // fail if fails, neutral is warnings, else success
                        conclusion: hasFails ? "failure" : hasWarnings ? "neutral" : "success",
                        // The rest of the vars, need to see this in prod to really make a
                        // nuanced take on what it should look like
                        output: {
                            title: isEmpty ? "All good" : "",
                            summary: mainBody,
                            annotations: annotations,
                        },
                    }];
        }
    });
}); };
var inlineResultsToAnnotations = function (results, options, getBlobUrlForPath) { return __awaiter(_this, void 0, void 0, function () {
    var inlineResults, annotations, _i, inlineResults_1, perFileResults, annotation, _a;
    return __generator(this, function (_b) {
        switch (_b.label) {
            case 0:
                inlineResults = DangerResults_1.resultsIntoInlineResults(results);
                annotations = [];
                _i = 0, inlineResults_1 = inlineResults;
                _b.label = 1;
            case 1:
                if (!(_i < inlineResults_1.length)) return [3 /*break*/, 4];
                perFileResults = inlineResults_1[_i];
                _a = {
                    filename: perFileResults.file
                };
                return [4 /*yield*/, getBlobUrlForPath(perFileResults.file)];
            case 2:
                annotation = (_a.blob_href = _b.sent(),
                    _a.warning_level = warningLevelForInlineResults(perFileResults),
                    _a.message = githubIssueTemplate_1.inlineTemplate(options.dangerID, DangerResults_1.inlineResultsIntoResults(perFileResults), perFileResults.file, perFileResults.line),
                    _a.start_line = perFileResults.line || 0,
                    _a.end_line = perFileResults.line || 0,
                    _a);
                annotations.push(annotation);
                _b.label = 3;
            case 3:
                _i++;
                return [3 /*break*/, 1];
            case 4: return [2 /*return*/, annotations];
        }
    });
}); };
var warningLevelForInlineResults = function (results) {
    var hasFails = results.fails.length > 0;
    var hasWarnings = results.warnings.length > 0;
    return hasFails ? "failure" : hasWarnings ? "warning" : "notice";
};
//# sourceMappingURL=resultsToCheck.js.map