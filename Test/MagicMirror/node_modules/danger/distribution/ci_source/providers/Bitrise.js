"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var ci_source_helpers_1 = require("../ci_source_helpers");
/**
 * ### CI Setup
 *  You need to edit your `bitrise.yml` (in version control, or directly from UI) to include `yarn danger ci`.
 *
 *   You can set "is_always_run: true" to ensure that it reports even if previous steps fails
 *
 *   ```yaml
 *     workflows:
 *       <your_workflow_name>:
 *         steps:
 *         - yarn:
 *           inputs:
 *           - args: ci
 *           - command: danger
 *           is_always_run: true
 *   ```
 *
 *  Adding this to your `bitrise.yml` allows Danger to fail your build, both on the Bitrise website and within your Pull Request.
 *  With that set up, you can edit your job to add `yarn danger ci` at the build action.
 *
 *  ### Token Setup
 *
 *  You need to add the `DANGER_GITHUB_API_TOKEN` environment variable, to do this,
 *  go to your repo's secrets, which should look like: `https://www.bitrise.io/app/[app_id]#/workflow` and secrets tab.
 *
 *  You should check the case "Expose for Pull Requests?".
 */
var Bitrise = /** @class */ (function () {
    function Bitrise(env) {
        this.env = env;
    }
    Object.defineProperty(Bitrise.prototype, "name", {
        get: function () {
            return "Bitrise";
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Bitrise.prototype, "isCI", {
        get: function () {
            return ci_source_helpers_1.ensureEnvKeysExist(this.env, ["BITRISE_IO"]);
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Bitrise.prototype, "isPR", {
        get: function () {
            var mustHave = ["GIT_REPOSITORY_URL"];
            var mustBeInts = ["BITRISE_PULL_REQUEST"];
            return ci_source_helpers_1.ensureEnvKeysExist(this.env, mustHave) && ci_source_helpers_1.ensureEnvKeysAreInt(this.env, mustBeInts);
        },
        enumerable: true,
        configurable: true
    });
    Bitrise.prototype._parseRepoURL = function () {
        var repoURL = this.env.GIT_REPOSITORY_URL;
        var regexp = new RegExp("([/:])([^/]+/[^/.]+)(?:.git)?$");
        var matches = repoURL.match(regexp);
        return matches ? matches[2] : "";
    };
    Object.defineProperty(Bitrise.prototype, "pullRequestID", {
        get: function () {
            return this.env.BITRISE_PULL_REQUEST;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Bitrise.prototype, "repoSlug", {
        get: function () {
            return this._parseRepoURL();
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Bitrise.prototype, "ciRunURL", {
        get: function () {
            return process.env.BITRISE_PULL_REQUEST;
        },
        enumerable: true,
        configurable: true
    });
    return Bitrise;
}());
exports.Bitrise = Bitrise;
//# sourceMappingURL=Bitrise.js.map