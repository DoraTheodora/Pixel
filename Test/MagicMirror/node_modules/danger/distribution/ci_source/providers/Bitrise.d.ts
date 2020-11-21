import { Env, CISource } from "../ci_source";
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
export declare class Bitrise implements CISource {
    private readonly env;
    constructor(env: Env);
    readonly name: string;
    readonly isCI: boolean;
    readonly isPR: boolean;
    private _parseRepoURL;
    readonly pullRequestID: string;
    readonly repoSlug: string;
    readonly ciRunURL: string | undefined;
}
