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
var gitJSONToGitDSL_1 = require("../git/gitJSONToGitDSL");
var debug_1 = require("../../debug");
var d = debug_1.debug("BitBucketServerGit");
/**
 * Returns the response for the new comment
 *
 * @param {BitBucketServerCommit} ghCommit A BitBucketServer based commit
 * @returns {GitCommit} a Git commit representation without GH metadata
 */
function bitBucketServerCommitToGitCommit(bbsCommit, repoMetadata, host) {
    var url = host + "/" + repoMetadata.repoSlug + "/commits/" + bbsCommit.id;
    return {
        sha: bbsCommit.id,
        parents: bbsCommit.parents.map(function (p) { return p.id; }),
        author: {
            email: bbsCommit.author.emailAddress,
            name: bbsCommit.author.name,
            date: new Date(bbsCommit.authorTimestamp).toISOString(),
        },
        committer: bbsCommit.committer
            ? {
                email: bbsCommit.committer.emailAddress,
                name: bbsCommit.committer.name,
                date: new Date(bbsCommit.committerTimestamp).toISOString(),
            }
            : {
                email: bbsCommit.author.emailAddress,
                name: bbsCommit.author.name,
                date: new Date(bbsCommit.authorTimestamp).toISOString(),
            },
        message: bbsCommit.message,
        tree: null,
        url: url,
    };
}
function gitDSLForBitBucketServer(api) {
    return __awaiter(this, void 0, void 0, function () {
        var diff, gitCommits, commits;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0: return [4 /*yield*/, api.getPullRequestDiff()];
                case 1:
                    diff = _a.sent();
                    return [4 /*yield*/, api.getPullRequestCommits()];
                case 2:
                    gitCommits = _a.sent();
                    commits = gitCommits.map(function (commit) {
                        return bitBucketServerCommitToGitCommit(commit, api.repoMetadata, api.repoCredentials.host);
                    });
                    return [2 /*return*/, bitBucketServerDiffToGitJSONDSL(diff, commits)];
            }
        });
    });
}
exports.default = gitDSLForBitBucketServer;
exports.bitBucketServerGitDSL = function (bitBucketServer, json, bitBucketServerAPI) {
    var config = {
        repo: "projects/" + bitBucketServer.pr.fromRef.repository.project.key + "/" +
            ("repos/" + bitBucketServer.pr.fromRef.repository.slug),
        baseSHA: bitBucketServer.pr.fromRef.latestCommit,
        headSHA: bitBucketServer.pr.toRef.latestCommit,
        getFileContents: bitBucketServerAPI.getFileContents,
        getFullStructuredDiff: function (base, head) { return __awaiter(_this, void 0, void 0, function () {
            var diff;
            return __generator(this, function (_a) {
                switch (_a.label) {
                    case 0: return [4 /*yield*/, bitBucketServerAPI.getStructuredDiff(base, head)];
                    case 1:
                        diff = _a.sent();
                        return [2 /*return*/, bitBucketServerDiffToGitStructuredDiff(diff)];
                }
            });
        }); },
    };
    d("Setting up git DSL with: ", config);
    return gitJSONToGitDSL_1.gitJSONToGitDSL(json, config);
};
var bitBucketServerDiffToGitJSONDSL = function (diffs, commits) {
    var deleted_files = diffs.filter(function (diff) { return diff.source && !diff.destination; }).map(function (diff) { return diff.source.toString; });
    var created_files = diffs.filter(function (diff) { return !diff.source && diff.destination; }).map(function (diff) { return diff.destination.toString; });
    var modified_files = diffs.filter(function (diff) { return diff.source && diff.destination; }).map(function (diff) { return diff.destination.toString; });
    return {
        modified_files: modified_files,
        created_files: created_files,
        deleted_files: deleted_files,
        commits: commits,
    };
};
var bitBucketServerDiffToGitStructuredDiff = function (diffs) {
    // We need all changed lines with it's type. It will convert hunk segment lines to flatten changed lines.
    var segmentValues = { ADDED: "add", CONTEXT: "normal", REMOVED: "del" };
    return diffs.map(function (diff) { return ({
        from: diff.source && diff.source.toString,
        to: diff.destination && diff.destination.toString,
        chunks: diff.hunks &&
            diff.hunks.map(function (hunk) { return ({
                changes: hunk.segments
                    .map(function (segment) {
                    return segment.lines.map(function (line) { return ({
                        type: segmentValues[segment.type],
                        content: line.line,
                        sourceLine: line.source,
                        destinationLine: line.destination,
                    }); });
                })
                    .reduce(function (a, b) { return a.concat(b); }, []),
            }); }),
    }); });
};
//# sourceMappingURL=BitBucketServerGit.js.map