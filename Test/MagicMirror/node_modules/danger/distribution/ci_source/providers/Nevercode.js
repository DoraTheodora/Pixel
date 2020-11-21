"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var ci_source_helpers_1 = require("../ci_source_helpers");
/**
 * Nevercode.io CI Integration
 *
 * Environment Variables Documented: https://developer.nevercode.io/v1.0/docs/environment-variables-files
 */
var Nevercode = /** @class */ (function () {
    function Nevercode(env) {
        this.env = env;
    }
    Object.defineProperty(Nevercode.prototype, "name", {
        get: function () {
            return "Nevercode";
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Nevercode.prototype, "isCI", {
        get: function () {
            return ci_source_helpers_1.ensureEnvKeysExist(this.env, ["NEVERCODE"]);
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Nevercode.prototype, "isPR", {
        get: function () {
            var mustHave = ["NEVERCODE_PULL_REQUEST", "NEVERCODE_REPO_SLUG"];
            var mustBeInts = ["NEVERCODE_GIT_PROVIDER_PULL_REQUEST", "NEVERCODE_PULL_REQUEST_NUMBER"];
            return (ci_source_helpers_1.ensureEnvKeysExist(this.env, mustHave) &&
                ci_source_helpers_1.ensureEnvKeysAreInt(this.env, mustBeInts) &&
                this.env.NEVERCODE_PULL_REQUEST == "true");
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Nevercode.prototype, "pullRequestID", {
        get: function () {
            return this.env.NEVERCODE_PULL_REQUEST_NUMBER;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Nevercode.prototype, "repoSlug", {
        get: function () {
            return this.env.NEVERCODE_REPO_SLUG;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Nevercode.prototype, "ciRunURL", {
        get: function () {
            return process.env.NEVERCODE_BUILD_URL;
        },
        enumerable: true,
        configurable: true
    });
    return Nevercode;
}());
exports.Nevercode = Nevercode;
//# sourceMappingURL=Nevercode.js.map