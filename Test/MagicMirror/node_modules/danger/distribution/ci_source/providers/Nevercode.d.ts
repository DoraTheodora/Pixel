import { Env, CISource } from "../ci_source";
/**
 * Nevercode.io CI Integration
 *
 * Environment Variables Documented: https://developer.nevercode.io/v1.0/docs/environment-variables-files
 */
export declare class Nevercode implements CISource {
    private readonly env;
    constructor(env: Env);
    readonly name: string;
    readonly isCI: boolean;
    readonly isPR: boolean;
    readonly pullRequestID: string;
    readonly repoSlug: string;
    readonly ciRunURL: string | undefined;
}
