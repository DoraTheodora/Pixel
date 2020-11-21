import { Env, CISource } from "../ci_source";
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
export declare class Jenkins implements CISource {
    private readonly env;
    constructor(env: Env);
    readonly name: string;
    readonly isCI: boolean;
    readonly isPR: boolean;
    readonly pullRequestID: string;
    readonly repoSlug: string;
    readonly ciRunURL: string | undefined;
}
