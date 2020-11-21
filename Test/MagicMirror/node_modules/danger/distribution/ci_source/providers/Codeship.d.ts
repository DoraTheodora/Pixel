import { Env, CISource } from "../ci_source";
/**
 * ### CI Setup
 *
 * To make Danger run, add a new step to the `codeship-steps.yml` file:
 *
 * ```
 * - type: parallel:
 *   ...
 *    - name: danger
 *      service: web
 *      command: yarn danger ci
 * ```
 *
 * If you're using Codeship Classic, add `yarn danger ci` to your 'Test Commands'
 *
 * ### Token Setup
 *
 * You'll want to edit your `codeship-services.yml` file to include a reference
 * to the Danger authentication token: `DANGER_GITHUB_API_TOKEN`.
 *
 * ```
 * project_name:
 *   ...
 *   environment:
 *     - DANGER_GITHUB_API_TOKEN=[my_token]
 * ```
 *
 * If you're using Codeship Classic, add `DANGER_GITHUB_API_TOKEN` to your
 * 'Environment' settings.
 */
export declare class Codeship implements CISource {
    private readonly env;
    private default;
    constructor(env: Env);
    setup(): Promise<any>;
    readonly name: string;
    readonly isCI: boolean;
    readonly isPR: boolean;
    readonly pullRequestID: string;
    readonly repoSlug: string;
    private readonly branchName;
}
