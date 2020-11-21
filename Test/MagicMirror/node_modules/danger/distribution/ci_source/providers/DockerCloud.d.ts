import { Env, CISource } from "../ci_source";
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
export declare class DockerCloud implements CISource {
    private readonly env;
    constructor(env: Env);
    readonly name: string;
    readonly isCI: boolean;
    readonly isPR: boolean;
    private _prParseURL;
    readonly pullRequestID: string;
    readonly repoSlug: string;
    readonly repoURL: string;
}
