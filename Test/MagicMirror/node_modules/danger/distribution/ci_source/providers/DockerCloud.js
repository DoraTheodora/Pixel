"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var ci_source_helpers_1 = require("../ci_source_helpers");
/**
 *
 * ### CI Setup
 *
 * You'll want to add danger to your existing `Dockerfile.test` (or whatever you
 * have choosen as your `sut` Dockerfile.)
 *
 * ```sh
 * ...
 *
 * CMD ["yarn", "danger"]
 * ```
 *
 * ### Token Setup
 *
 * #### GitHub
 *
 * Your `DANGER_GITHUB_API_TOKEN` will need to be exposed to the `sut` part of your
 * `docker-compose.yml`.  This looks similar to:
 *
 * ```
 * sut:
 *   ...
 *   environment:
 *     - DANGER_GITHUB_API_TOKEN=[my_token]
 * ```
 */
var DockerCloud = /** @class */ (function () {
    function DockerCloud(env) {
        this.env = env;
    }
    Object.defineProperty(DockerCloud.prototype, "name", {
        get: function () {
            return "Docker Cloud";
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(DockerCloud.prototype, "isCI", {
        get: function () {
            return ci_source_helpers_1.ensureEnvKeysExist(this.env, ["DOCKER_REPO"]);
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(DockerCloud.prototype, "isPR", {
        get: function () {
            if (ci_source_helpers_1.ensureEnvKeysExist(this.env, ["PULL_REQUEST_URL"])) {
                return true;
            }
            var mustHave = ["SOURCE_REPOSITORY_URL", "PULL_REQUEST_URL"];
            return ci_source_helpers_1.ensureEnvKeysExist(this.env, mustHave);
        },
        enumerable: true,
        configurable: true
    });
    DockerCloud.prototype._prParseURL = function () {
        var prUrl = this.env.PULL_REQUEST_URL || "";
        var splitSlug = prUrl.split("/");
        if (splitSlug.length === 7) {
            var owner = splitSlug[3];
            var reponame = splitSlug[4];
            var id = splitSlug[6];
            return { owner: owner, reponame: reponame, id: id };
        }
        return {};
    };
    Object.defineProperty(DockerCloud.prototype, "pullRequestID", {
        get: function () {
            var id = this._prParseURL().id;
            return id || "";
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(DockerCloud.prototype, "repoSlug", {
        get: function () {
            var _a = this._prParseURL(), owner = _a.owner, reponame = _a.reponame;
            return owner && reponame ? owner + "/" + reponame : "";
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(DockerCloud.prototype, "repoURL", {
        get: function () {
            return this.env.SOURCE_REPOSITORY_URL;
        },
        enumerable: true,
        configurable: true
    });
    return DockerCloud;
}());
exports.DockerCloud = DockerCloud;
//# sourceMappingURL=DockerCloud.js.map