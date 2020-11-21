"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var parseGitConfig = require("parse-git-config");
var parseGithubURL = require("parse-github-url");
exports.getRepoSlug = function () {
    var config = parseGitConfig.sync();
    var possibleRemotes = [config['remote "upstream"'], config['remote "origin"']].filter(function (f) { return f; });
    if (possibleRemotes.length === 0) {
        return null;
    }
    var ghData = possibleRemotes.map(function (r) { return parseGithubURL(r.url); });
    return ghData.length ? ghData[0].repo : undefined;
};
//# sourceMappingURL=get-repo-slug.js.map