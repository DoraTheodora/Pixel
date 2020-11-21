"use strict";
var __assign = (this && this.__assign) || function () {
    __assign = Object.assign || function(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p))
                t[p] = s[p];
        }
        return t;
    };
    return __assign.apply(this, arguments);
};
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
var GitHubNodeAPI = require("@octokit/rest");
var GitHubGit_1 = require("../platforms/github/GitHubGit");
var GitHub_1 = require("../platforms/GitHub");
var DangerUtils_1 = require("./DangerUtils");
var LocalGit_1 = require("../platforms/LocalGit");
var BitBucketServerGit_1 = require("../platforms/bitbucket_server/BitBucketServerGit");
var BitBucketServerAPI_1 = require("../platforms/bitbucket_server/BitBucketServerAPI");
exports.jsonToDSL = function (dsl) { return __awaiter(_this, void 0, void 0, function () {
    var api, platformExists, github, bitbucket_server, git, localPlatform;
    return __generator(this, function (_a) {
        switch (_a.label) {
            case 0:
                api = apiForDSL(dsl);
                platformExists = [dsl.github, dsl.bitbucket_server].some(function (p) { return !!p; });
                github = dsl.github && GitHub_1.githubJSONToGitHubDSL(dsl.github, api);
                bitbucket_server = dsl.bitbucket_server;
                if (!!platformExists) return [3 /*break*/, 2];
                localPlatform = new LocalGit_1.LocalGit(dsl.settings.cliArgs);
                return [4 /*yield*/, localPlatform.getPlatformGitRepresentation()];
            case 1:
                git = _a.sent();
                return [3 /*break*/, 3];
            case 2:
                if (process.env["DANGER_BITBUCKETSERVER_HOST"]) {
                    git = BitBucketServerGit_1.bitBucketServerGitDSL(bitbucket_server, dsl.git, api);
                }
                else {
                    git = GitHubGit_1.gitHubGitDSL(github, dsl.git);
                }
                _a.label = 3;
            case 3: return [2 /*return*/, {
                    git: git,
                    // Strictly speaking, this is a lie. Only one of these will _ever_ exist, but
                    // otherwise everyone would need to have a check for GitHub/BBS in every Dangerfile
                    // which just doesn't feel right.
                    github: github,
                    bitbucket_server: bitbucket_server,
                    utils: {
                        sentence: DangerUtils_1.sentence,
                        href: DangerUtils_1.href,
                    },
                }];
        }
    });
}); };
var apiForDSL = function (dsl) {
    if (process.env["DANGER_BITBUCKETSERVER_HOST"]) {
        return new BitBucketServerAPI_1.BitBucketServerAPI(dsl.bitbucket_server.metadata, BitBucketServerAPI_1.bitbucketServerRepoCredentialsFromEnv(process.env));
    }
    var options = {
        debug: !!process.env.LOG_FETCH_REQUESTS,
        baseUrl: dsl.settings.github.baseURL,
        headers: __assign({}, dsl.settings.github.additionalHeaders),
    };
    var api = new GitHubNodeAPI(options);
    if (dsl.settings.github && dsl.settings.github.accessToken) {
        api.authenticate({ type: "token", token: dsl.settings.github.accessToken });
    }
    return api;
};
//# sourceMappingURL=jsonToDSL.js.map