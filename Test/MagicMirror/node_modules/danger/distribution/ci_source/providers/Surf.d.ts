import { Env, CISource } from "../ci_source";
/**
 *  ### CI Setup
 *
 *  You want to add `yarn danger ci` to your `build.sh` file to run  Danger at the
 *  end of your build.
 *
 *  ### Token Setup
 *
 *  As this is self-hosted, you will need to add the `DANGER_GITHUB_API_TOKEN` to your build user's ENV. The alternative
 *  is to pass in the token as a prefix to the command `DANGER_GITHUB_API_TOKEN="123" yarn danger ci`.
 */
export declare class Surf implements CISource {
    private readonly env;
    constructor(env: Env);
    readonly name: string;
    readonly isCI: boolean;
    readonly isPR: boolean;
    readonly pullRequestID: string;
    readonly repoSlug: string;
}
