import * as node_fetch from "node-fetch";
import { BitBucketServerPRDSL, BitBucketServerCommit, BitBucketServerPRComment, JIRAIssue, BitBucketServerPRActivity, BitBucketServerDiff, RepoMetaData } from "../../dsl/BitBucketServerDSL";
import { Comment } from "../platform";
import { Env } from "../../ci_source/ci_source";
import { api as fetch } from "../../api/fetch";
export interface BitBucketRepoCredentials {
    host: string;
    username?: string;
    password?: string;
}
export declare function bitbucketServerRepoCredentialsFromEnv(env: Env): BitBucketRepoCredentials;
/** This represent the BitBucketServer API */
export declare class BitBucketServerAPI {
    readonly repoMetadata: RepoMetaData;
    readonly repoCredentials: BitBucketRepoCredentials;
    fetch: typeof fetch;
    private readonly d;
    private pr;
    constructor(repoMetadata: RepoMetaData, repoCredentials: BitBucketRepoCredentials);
    getPRBasePath(service?: string): string;
    getPullRequestsFromBranch: (branch: string) => Promise<BitBucketServerPRDSL[]>;
    getPullRequestInfo: () => Promise<BitBucketServerPRDSL>;
    getPullRequestCommits: () => Promise<BitBucketServerCommit[]>;
    getStructuredDiff: (base: string, head: string) => Promise<BitBucketServerDiff[]>;
    getPullRequestDiff: () => Promise<BitBucketServerDiff[]>;
    getPullRequestComments: () => Promise<BitBucketServerPRActivity[]>;
    getPullRequestActivities: () => Promise<BitBucketServerPRActivity[]>;
    getIssues: () => Promise<JIRAIssue[]>;
    getDangerComments: (dangerID: string) => Promise<BitBucketServerPRComment[]>;
    getDangerInlineComments: (dangerID: string) => Promise<Comment[]>;
    getFileContents: (filePath: string, repoSlug?: string | undefined, refspec?: string | undefined) => Promise<string>;
    postBuildStatus: (commitId: string, payload: {
        state: string;
        key: string;
        name: string;
        url: string;
        description: string;
    }) => Promise<any>;
    postPRComment: (comment: string) => Promise<any>;
    postInlinePRComment: (comment: string, line: number, type: string, filePath: string) => Promise<any>;
    deleteComment: ({ id, version }: BitBucketServerPRComment) => Promise<void>;
    updateComment: ({ id, version }: BitBucketServerPRComment, comment: string) => Promise<any>;
    private api;
    get: (path: string, headers?: any, suppressErrors?: boolean | undefined) => Promise<node_fetch.Response>;
    post: (path: string, headers?: any, body?: any, suppressErrors?: boolean | undefined) => Promise<node_fetch.Response>;
    put: (path: string, headers?: any, body?: any) => Promise<node_fetch.Response>;
    delete: (path: string, headers?: any, body?: any) => Promise<node_fetch.Response>;
}
