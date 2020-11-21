"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var ci_source_helpers_1 = require("../ci_source_helpers");
/**
 * ### CI Setup
 *
 * Buddybuild has an integration for Danger JS already built-in.
 *
 * ### Token Setup
 *
 * Login to buddybuild and select your app. Go to your *App Settings* and
 * in the *Build Settings* menu on the left, choose *Environment Variables*.
 *
 * #### GitHub
 * Add the `DANGER_GITHUB_API_TOKEN` to your build user's ENV.
 *
 */
var BuddyBuild = /** @class */ (function () {
    function BuddyBuild(env) {
        this.env = env;
    }
    Object.defineProperty(BuddyBuild.prototype, "name", {
        get: function () {
            return "buddybuild";
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(BuddyBuild.prototype, "isCI", {
        get: function () {
            return ci_source_helpers_1.ensureEnvKeysExist(this.env, ["BUDDYBUILD_BUILD_ID"]);
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(BuddyBuild.prototype, "isPR", {
        get: function () {
            var mustHave = ["BUDDYBUILD_PULL_REQUEST", "BUDDYBUILD_REPO_SLUG"];
            var mustBeInts = ["BUDDYBUILD_PULL_REQUEST"];
            return ci_source_helpers_1.ensureEnvKeysExist(this.env, mustHave) && ci_source_helpers_1.ensureEnvKeysAreInt(this.env, mustBeInts);
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(BuddyBuild.prototype, "pullRequestID", {
        get: function () {
            return this.env.BUDDYBUILD_PULL_REQUEST;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(BuddyBuild.prototype, "repoSlug", {
        get: function () {
            return this.env.BUDDYBUILD_REPO_SLUG;
        },
        enumerable: true,
        configurable: true
    });
    return BuddyBuild;
}());
exports.BuddyBuild = BuddyBuild;
//# sourceMappingURL=BuddyBuild.js.map