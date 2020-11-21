"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var buildHeader = function (headers) {
    return "| " + headers.join(" | ") + " |\n" + ("| " + headers.map(function (_) { return "---"; }).join(" | ") + " |");
};
var buildRow = function (row) { return "| " + row.join(" | ") + " |"; };
var buildRows = function (rows) { return rows.map(buildRow).join("\n"); };
function template(headers, rows) {
    return buildHeader(headers) + "\n" + ("" + buildRows(rows));
}
exports.template = template;
//# sourceMappingURL=markdownTableTemplate.js.map