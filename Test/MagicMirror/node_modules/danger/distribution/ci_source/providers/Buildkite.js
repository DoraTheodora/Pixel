"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var ci_source_helpers_1 = require("../ci_source_helpers");
/**
 * ### CI Setup
 *
 * With BuildKite you run the server yourself, so you will want to run  it as a part of your build process.
 * It is common to have build steps, so we would recommend adding this to your scrip:
 *
 *  ``` shell
 *   echo "--- Running Danger"
 *   bundle exec danger
 *  ```
 *
 * ### Token Setup
 *
 * #### GitHub
 *
 * As this is self-hosted, you will need to add the `DANGER_GITHUB_API_TOKEN` to your build user's ENV. The  alternative
 * is to pass in the token as a prefix to the command `DANGER_GITHUB_API_TOKEN="123" bundle exec danger`.
 */
var Buildkite = /** @class */ (function () {
    function Buildkite(env) {
        this.env = env;
    }
    Object.defineProperty(Buildkite.prototype, "name", {
        get: function () {
            return "Buildkite";
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Buildkite.prototype, "isCI", {
        get: function () {
            return ci_source_helpers_1.ensureEnvKeysExist(this.env, ["BUILDKITE"]);
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Buildkite.prototype, "isPR", {
        get: function () {
            var mustHave = ["BUILDKITE_REPO"];
            var mustBeInts = ["BUILDKITE_PULL_REQUEST"];
            return ci_source_helpers_1.ensureEnvKeysExist(this.env, mustHave) && ci_source_helpers_1.ensureEnvKeysAreInt(this.env, mustBeInts);
        },
        enumerable: true,
        configurable: true
    });
    Buildkite.prototype._parseRepoURL = function () {
        var repoURL = this.env.BUILDKITE_REPO;
        var regexp = new RegExp("([/:])([^/]+/[^/.]+)(?:.git)?$");
        var matches = repoURL.match(regexp);
        return matches ? matches[2] : "";
    };
    Object.defineProperty(Buildkite.prototype, "pullRequestID", {
        get: function () {
            return this.env.BUILDKITE_PULL_REQUEST;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Buildkite.prototype, "repoSlug", {
        get: function () {
            return this._parseRepoURL();
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Buildkite.prototype, "ciRunURL", {
        get: function () {
            return process.env.BUILDKITE_BUILD_URL;
        },
        enumerable: true,
        configurable: true
    });
    return Buildkite;
}());
exports.Buildkite = Buildkite;
//# sourceMappingURL=Buildkite.js.map