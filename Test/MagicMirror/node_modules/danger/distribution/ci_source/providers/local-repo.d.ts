import { Env, CISource } from "../ci_source";
export declare class LocalRepo implements CISource {
    private readonly env;
    constructor(env: Env);
    readonly name: string;
    readonly isCI: boolean;
    readonly isPR: boolean;
    readonly pullRequestID: string;
    readonly repoSlug: string;
}
