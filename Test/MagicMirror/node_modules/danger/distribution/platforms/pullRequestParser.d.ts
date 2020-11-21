export interface PullRequestParts {
    pullRequestNumber: string;
    repo: string;
}
export declare function pullRequestParser(address: string): PullRequestParts | null;
