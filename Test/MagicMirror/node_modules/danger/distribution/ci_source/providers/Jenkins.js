"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var ci_source_helpers_1 = require("../ci_source_helpers");
// https://jenkins.io/
// https://wiki.jenkins.io/display/JENKINS/Building+a+software+project#Buildingasoftwareproject-belowJenkinsSetEnvironmentVariables
/**
 * ### CI Setup
 * Ah Jenkins, so many memories. So, if you're using Jenkins, you're hosting your own environment.
 *
 * ### GitHub
 * You will want to be using the
 * [GitHub pull request builder plugin](https://wiki.jenkins.io/display/JENKINS/GitHub+pull+request+builder+plugin)
 * in order to ensure that you have the build environment set up for PR integration.
 *
 * ### BitBucket Server
 * If using Bitbucket Server, make sure to provide both `ghprbGhRepository` and `ghprbPullId` as environment variables.
 * `ghprbGhRepository` is the path to your repository, e.g. `projects/team/repos/repositoryname`, while `ghprbPullId`
 * provides the id of a pull request (usually `env.CHANGE_ID`). Danger will skip execution if this id is not provided.
 *
 * With that set up, you can edit your job to add `yarn danger ci` at the build action.
 *
 * ### Pipeline
 * If you're using [pipelines](https://jenkins.io/solutions/pipeline/) you should be using the
 * [GitHub branch source plugin](https://wiki.jenkins.io/display/JENKINS/GitHub+Branch+Source+Plugin) for easy setup and handling of PRs.
 *
 * After you've set up the plugin, add a `sh 'yarn danger ci'` line in your pipeline script and make sure that build PRs is enabled.
 *
 * ## Token Setup
 *
 * ### GitHub
 * As you own the machine, it's up to you to add the environment variable for the `DANGER_GITHUB_API_TOKEN`.
 */
var Jenkins = /** @class */ (function () {
    function Jenkins(env) {
        this.env = env;
    }
    Object.defineProperty(Jenkins.prototype, "name", {
        get: function () {
            return "Jenkins";
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Jenkins.prototype, "isCI", {
        get: function () {
            return ci_source_helpers_1.ensureEnvKeysExist(this.env, ["JENKINS_URL"]);
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Jenkins.prototype, "isPR", {
        get: function () {
            var mustHave = ["JENKINS_URL", "ghprbPullId", "ghprbGhRepository"];
            var mustBeInts = ["ghprbPullId"];
            return ci_source_helpers_1.ensureEnvKeysExist(this.env, mustHave) && ci_source_helpers_1.ensureEnvKeysAreInt(this.env, mustBeInts);
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Jenkins.prototype, "pullRequestID", {
        get: function () {
            return this.env.ghprbPullId;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Jenkins.prototype, "repoSlug", {
        get: function () {
            return this.env.ghprbGhRepository;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Jenkins.prototype, "ciRunURL", {
        get: function () {
            return process.env.BUILD_URL;
        },
        enumerable: true,
        configurable: true
    });
    return Jenkins;
}());
exports.Jenkins = Jenkins;
//# sourceMappingURL=Jenkins.js.map