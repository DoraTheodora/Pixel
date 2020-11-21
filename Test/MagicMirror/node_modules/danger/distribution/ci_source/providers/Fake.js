"use strict";
var __assign = (this && this.__assign) || function () {
    __assign = Object.assign || function(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p))
                t[p] = s[p];
        }
        return t;
    };
    return __assign.apply(this, arguments);
};
Object.defineProperty(exports, "__esModule", { value: true });
var ci_source_helpers_1 = require("../ci_source_helpers");
var FakeCI = /** @class */ (function () {
    function FakeCI(env) {
        var defaults = {
            repo: env.DANGER_TEST_REPO || "artsy/emission",
            pr: env.DANGER_TEST_PR || "327",
        };
        this.env = __assign({}, env, defaults);
    }
    Object.defineProperty(FakeCI.prototype, "name", {
        get: function () {
            return "Fake Testing CI";
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(FakeCI.prototype, "isCI", {
        get: function () {
            return ci_source_helpers_1.ensureEnvKeysExist(this.env, ["DANGER_FAKE_CI"]);
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(FakeCI.prototype, "isPR", {
        get: function () {
            return true;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(FakeCI.prototype, "pullRequestID", {
        get: function () {
            return this.env.pr;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(FakeCI.prototype, "repoSlug", {
        get: function () {
            return this.env.repo;
        },
        enumerable: true,
        configurable: true
    });
    return FakeCI;
}());
exports.FakeCI = FakeCI;
//# sourceMappingURL=Fake.js.map