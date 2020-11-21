import { Env, CISource } from "../ci_source";
/**
 *  ### CI Setup
 *
 *  For setting up Circle CI, we recommend turning on "Only Build pull requests." in "Advanced Setting." Without this enabled,
 *  it is _really_ tricky for Danger to know whether you are in a pull request or not, as the environment metadata
 *  isn't reliable. This may be different with Circle v2.
 *
 *  With that set up, you can you add `yarn danger ci` to your `circle.yml`. If you override the default
 *  `test:` section, then add it as an extra step. Otherwise add a new `pre` section to the test:
 *
 *    ``` ruby
 *    test:
 *      override:
 *          - yarn danger ci
 *    ```
 *
 *  ### Token Setup
 *
 *  There is no difference here for OSS vs Closed, add your `DANGER_GITHUB_API_TOKEN` to the Environment variable settings page.
 *
 */
export declare class Circle implements CISource {
    private readonly env;
    constructor(env: Env);
    readonly name: string;
    readonly isCI: boolean;
    readonly isPR: boolean;
    private _prParseURL;
    readonly pullRequestID: string;
    readonly repoSlug: string;
    readonly repoURL: string;
    readonly ciRunURL: any;
}
