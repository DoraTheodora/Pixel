"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var ci_source_helpers_1 = require("../ci_source_helpers");
/**
 *  ### CI Setup
 *
 *  For Semaphore you will want to go to the settings page of the project. Inside "Build Settings"
 *  you should add `yarn danger ci` to the Setup thread. Note that Semaphore only provides
 *  the build environment variables necessary for Danger on PRs across forks.
 *
 *  ### Token Setup
 *
 *  You can add your `DANGER_GITHUB_API_TOKEN` inside the "Environment Variables" section in the settings.
 *
 */
var Semaphore = /** @class */ (function () {
    function Semaphore(env) {
        this.env = env;
    }
    Object.defineProperty(Semaphore.prototype, "name", {
        get: function () {
            return "Semaphore";
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Semaphore.prototype, "isCI", {
        get: function () {
            return ci_source_helpers_1.ensureEnvKeysExist(this.env, ["SEMAPHORE"]);
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Semaphore.prototype, "isPR", {
        get: function () {
            var mustHave = ["SEMAPHORE_REPO_SLUG"];
            var mustBeInts = ["PULL_REQUEST_NUMBER"];
            return ci_source_helpers_1.ensureEnvKeysExist(this.env, mustHave) && ci_source_helpers_1.ensureEnvKeysAreInt(this.env, mustBeInts);
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Semaphore.prototype, "pullRequestID", {
        get: function () {
            return this.env.PULL_REQUEST_NUMBER;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Semaphore.prototype, "repoSlug", {
        get: function () {
            return this.env.SEMAPHORE_REPO_SLUG;
        },
        enumerable: true,
        configurable: true
    });
    return Semaphore;
}());
exports.Semaphore = Semaphore;
//# sourceMappingURL=Semaphore.js.map