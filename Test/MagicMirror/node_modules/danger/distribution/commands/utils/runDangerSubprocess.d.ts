import { DangerDSLJSONType } from "../../dsl/DangerDSL";
import { Executor } from "../../runner/Executor";
export declare const prepareDangerDSL: (dangerDSL: DangerDSLJSONType) => string;
declare const runDangerSubprocess: (subprocessName: string[], dslJSON: DangerDSLJSONType, exec: Executor) => void;
export default runDangerSubprocess;
