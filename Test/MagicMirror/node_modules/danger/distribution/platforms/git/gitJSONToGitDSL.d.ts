import { GitDSL, GitJSONDSL } from "../../dsl/GitDSL";
export interface GitJSONToGitDSLConfig {
    /** This is used in getFileContents to figure out your repo  */
    repo?: string;
    /** The sha things are going into */
    baseSHA: string;
    /** The sha which we're merging */
    headSHA: string;
    /** A promise which will return the string content of a file at a sha */
    getFileContents: (path: string, repo: string | undefined, sha: string) => Promise<string>;
    /** A promise which will return the diff string content for a file between shas */
    getFullDiff?: (base: string, head: string) => Promise<string>;
    getFullStructuredDiff?: (base: string, head: string) => Promise<GitStructuredDiff>;
}
export declare type GitStructuredDiff = {
    from?: string;
    to?: string;
    chunks: Chunk[];
}[];
export interface Chunk {
    changes: Changes;
}
export declare type Changes = {
    type: "add" | "del" | "normal";
    content: string;
}[];
export declare const gitJSONToGitDSL: (gitJSONRep: GitJSONDSL, config: GitJSONToGitDSLConfig) => GitDSL;
