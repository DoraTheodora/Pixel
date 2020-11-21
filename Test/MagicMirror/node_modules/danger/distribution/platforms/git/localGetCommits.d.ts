import { GitCommit } from "../../dsl/Commit";
export declare const formatJSON: string;
export declare const localGetCommits: (base: string, head: string) => Promise<GitCommit[]>;
