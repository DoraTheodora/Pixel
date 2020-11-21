import { Platform } from "../../platforms/platform";
import { SharedCLI } from "../utils/sharedDangerfileArgs";
import { CISource } from "../../ci_source/ci_source";
export interface RunnerConfig {
    source?: CISource;
    platform?: Platform;
    additionalArgs?: string[];
}
export declare const runRunner: (app: SharedCLI, config?: RunnerConfig | undefined) => Promise<void>;
