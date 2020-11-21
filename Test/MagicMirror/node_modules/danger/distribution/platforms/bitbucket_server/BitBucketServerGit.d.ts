import { GitDSL, GitJSONDSL } from "../../dsl/GitDSL";
import { BitBucketServerDSL } from "../../dsl/BitBucketServerDSL";
import { BitBucketServerAPI } from "../bitbucket_server/BitBucketServerAPI";
export default function gitDSLForBitBucketServer(api: BitBucketServerAPI): Promise<GitJSONDSL>;
export declare const bitBucketServerGitDSL: (bitBucketServer: BitBucketServerDSL, json: GitJSONDSL, bitBucketServerAPI: BitBucketServerAPI) => GitDSL;
