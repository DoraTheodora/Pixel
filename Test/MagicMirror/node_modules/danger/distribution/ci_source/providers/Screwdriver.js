"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var ci_source_helpers_1 = require("../ci_source_helpers");
/**
 * ### CI Setup
 *
 * Install dependencies and add a danger step to your screwdriver.yaml:
 * ``` yml
 * jobs:
 *   danger:
 *     requires: [~pr, ~commit]
 *     steps:
 *       - setup: yarn install
 *       - danger: yarn danger ci
 *     secrets:
 *       - DANGER_GITHUB_API_TOKEN
 * ```
 *
 * ### Token Setup
 *
 * Add the `DANGER_GITHUB_API_TOKEN` to your pipeline env as a
 * [build secret](https://docs.screwdriver.cd/user-guide/configuration/secrets)
 */
var Screwdriver = /** @class */ (function () {
    function Screwdriver(env) {
        this.env = env;
    }
    Object.defineProperty(Screwdriver.prototype, "name", {
        get: function () {
            return "Screwdriver";
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Screwdriver.prototype, "isCI", {
        get: function () {
            return ci_source_helpers_1.ensureEnvKeysExist(this.env, ["SCREWDRIVER"]);
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Screwdriver.prototype, "isPR", {
        get: function () {
            var mustHave = ["SCM_URL"];
            var mustBeInts = ["SD_PULL_REQUEST"];
            return ci_source_helpers_1.ensureEnvKeysExist(this.env, mustHave) && ci_source_helpers_1.ensureEnvKeysAreInt(this.env, mustBeInts);
        },
        enumerable: true,
        configurable: true
    });
    Screwdriver.prototype._parseRepoURL = function () {
        var repoURL = this.env.SCM_URL;
        var regexp = new RegExp("([/:])([^/]+/[^/.]+)(?:.git)?$");
        var matches = repoURL.match(regexp);
        return matches ? matches[2] : "";
    };
    Object.defineProperty(Screwdriver.prototype, "pullRequestID", {
        get: function () {
            return this.env.SD_PULL_REQUEST;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Screwdriver.prototype, "repoSlug", {
        get: function () {
            return this._parseRepoURL();
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Screwdriver.prototype, "ciRunURL", {
        get: function () {
            return process.env.BUILDKITE_BUILD_URL;
        },
        enumerable: true,
        configurable: true
    });
    return Screwdriver;
}());
exports.Screwdriver = Screwdriver;
//# sourceMappingURL=Screwdriver.js.map