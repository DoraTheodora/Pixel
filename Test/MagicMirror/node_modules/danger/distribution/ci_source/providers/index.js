"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var Bitrise_1 = require("./Bitrise");
var BuddyBuild_1 = require("./BuddyBuild");
var Buildkite_1 = require("./Buildkite");
var Circle_1 = require("./Circle");
var Codeship_1 = require("./Codeship");
var Concourse_1 = require("./Concourse");
var DockerCloud_1 = require("./DockerCloud");
var Drone_1 = require("./Drone");
var Fake_1 = require("./Fake");
var Jenkins_1 = require("./Jenkins");
var Nevercode_1 = require("./Nevercode");
var Semaphore_1 = require("./Semaphore");
var Surf_1 = require("./Surf");
var TeamCity_1 = require("./TeamCity");
var Travis_1 = require("./Travis");
var VSTS_1 = require("./VSTS");
var Screwdriver_1 = require("./Screwdriver");
var providers = [
    Travis_1.Travis,
    Circle_1.Circle,
    Semaphore_1.Semaphore,
    Nevercode_1.Nevercode,
    Jenkins_1.Jenkins,
    Fake_1.FakeCI,
    Surf_1.Surf,
    DockerCloud_1.DockerCloud,
    Codeship_1.Codeship,
    Drone_1.Drone,
    Buildkite_1.Buildkite,
    BuddyBuild_1.BuddyBuild,
    VSTS_1.VSTS,
    Bitrise_1.Bitrise,
    TeamCity_1.TeamCity,
    Screwdriver_1.Screwdriver,
    Concourse_1.Concourse,
];
exports.providers = providers;
// Mainly used for Dangerfile linting
var realProviders = [
    Travis_1.Travis,
    Circle_1.Circle,
    Semaphore_1.Semaphore,
    Nevercode_1.Nevercode,
    Jenkins_1.Jenkins,
    Surf_1.Surf,
    DockerCloud_1.DockerCloud,
    Codeship_1.Codeship,
    Drone_1.Drone,
    Buildkite_1.Buildkite,
    BuddyBuild_1.BuddyBuild,
    VSTS_1.VSTS,
    TeamCity_1.TeamCity,
    Screwdriver_1.Screwdriver,
    Concourse_1.Concourse,
];
exports.realProviders = realProviders;
//# sourceMappingURL=index.js.map