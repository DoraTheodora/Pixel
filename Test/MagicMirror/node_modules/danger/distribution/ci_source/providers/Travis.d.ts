import { Env, CISource } from "../ci_source";
/**
 * ### CI Setup
 *  You need to edit your `.travis.yml` to include `yarn danger ci`. If you already have
 *  a `script:` section then we recommend adding this command at the end of the script step: `- yarn danger ci`.
 *
 *   Otherwise, add a `before_script` step to the root of the `.travis.yml` with `yarn danger ci`
 *
 *   ```ruby
 *     before_script:
 *       - yarn danger ci
 *   ```
 *
 *  Adding this to your `.travis.yml` allows Danger to fail your build, both on the TravisCI website and within your Pull Request.
 *  With that set up, you can edit your job to add `yarn danger ci` at the build action.
 *
 *  ### Token Setup
 *
 *  You need to add the `DANGER_GITHUB_API_TOKEN` environment variable, to do this,
 *  go to your repo's settings, which should look like: `https://travis-ci.org/[user]/[repo]/settings`.
 *
 *  If you have an open source project, you should ensure "Display value in build log" enabled, so that PRs from forks work.
 */
export declare class Travis implements CISource {
    private readonly env;
    constructor(env: Env);
    readonly name: string;
    readonly isCI: boolean;
    readonly isPR: boolean;
    readonly pullRequestID: string;
    readonly repoSlug: string;
    readonly ciRunURL: string;
}
