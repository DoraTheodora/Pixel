import { Env, CISource } from "../ci_source";
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
export declare class Buildkite implements CISource {
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
