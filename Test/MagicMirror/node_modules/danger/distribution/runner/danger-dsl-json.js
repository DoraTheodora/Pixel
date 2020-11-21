"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
/**
 * Using the input JSON create an DangerDSL
 *
 * @see DangerDSLJSONType for more detailed definition
 */
var DangerDSLJSON = /** @class */ (function () {
    /**
     * Parse the JSON and assign danger to this object
     *
     * Also add the arguments sent to the CLI
     *
     * @param JSONString DSL in JSON format
     * @param cliArgs arguments used running danger command
     */
    function DangerDSLJSON(JSONString, cliArgs) {
        var parsedString = JSON.parse(JSONString);
        Object.assign(this, parsedString.danger);
        // @ts-ignore
        this.settings.cliArgs = cliArgs;
    }
    return DangerDSLJSON;
}());
exports.DangerDSLJSON = DangerDSLJSON;
//# sourceMappingURL=danger-dsl-json.js.map