import { Env, CISource } from "../ci_source";
/**
 * ### CI Setup
 *  You'll need to add a npm build step and set the custom command to "run danger"
 *
 *  Only supports VSTS with github as the repository, danger doesn't yet support VSTS as a repository platform
 *
 *  ### Token Setup
 *
 *  You need to add the `DANGER_GITHUB_API_TOKEN` environment variable
 */
export declare class VSTS implements CISource {
    private readonly env;
    constructor(env: Env);
    readonly name: string;
    readonly isCI: boolean;
    readonly isPR: boolean;
    readonly pullRequestID: string;
    readonly repoSlug: string;
}
