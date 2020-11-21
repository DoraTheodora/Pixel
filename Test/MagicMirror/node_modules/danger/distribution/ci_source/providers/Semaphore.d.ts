import { Env, CISource } from "../ci_source";
/**
 *  ### CI Setup
 *
 *  For Semaphore you will want to go to the settings page of the project. Inside "Build Settings"
 *  you should add `yarn danger ci` to the Setup thread. Note that Semaphore only provides
 *  the build environment variables necessary for Danger on PRs across forks.
 *
 *  ### Token Setup
 *
 *  You can add your `DANGER_GITHUB_API_TOKEN` inside the "Environment Variables" section in the settings.
 *
 */
export declare class Semaphore implements CISource {
    private readonly env;
    constructor(env: Env);
    readonly name: string;
    readonly isCI: boolean;
    readonly isPR: boolean;
    readonly pullRequestID: string;
    readonly repoSlug: string;
}
