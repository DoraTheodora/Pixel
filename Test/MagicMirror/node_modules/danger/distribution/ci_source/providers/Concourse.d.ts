import { Env, CISource } from "../ci_source";
/**
 * Concourse CI Integration
 *
 * https://concourse-ci.org/
 *
 *  ### CI Setup
 *
 *  With Concourse, you run the docker images yourself, so you will want to add `yarn danger ci` within one of your build jobs.
 *
 *   ``` shell
 *    build:
 *      image: golang
 *        commands:
 *          - ...
 *          - yarn danger ci
 *   ```
 *
 *  ### Environment Variable Setup
 *
 *  As this is self-hosted, you will need to add the `CONCOURSE` environment variable `export CONCOURSE=true` to your build environment,
 *  as well as setting environment variables for `PULL_REQUEST_ID` and `REPO_SLUG`. Assuming you are using the github pull request resource
 *  https://github.com/jtarchie/github-pullrequest-resource the id of the PR can be accessed from `git config --get pullrequest.id`.
 *
 *  ### Token Setup
 *
 *  Once again as this is self-hosted, you will need to add `DANGER_GITHUB_API_TOKEN` environment variable to the build environment.
 *  The suggested method of storing the token is within the vault - https://concourse-ci.org/creds.html
 */
export declare class Concourse implements CISource {
    private readonly env;
    constructor(env: Env);
    readonly name: string;
    readonly isCI: boolean;
    readonly isPR: boolean;
    readonly pullRequestID: string;
    readonly repoSlug: string;
    readonly ciRunURL: any;
}
