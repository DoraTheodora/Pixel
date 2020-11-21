import * as node_fetch from "node-fetch";
/**
 * Adds logging to every fetch request if a global var for `verbose` is set to true
 *
 * @param {(string | fetch.Request)} url the request
 * @param {fetch.RequestInit} [init] the usual options
 * @returns {Promise<fetch.Response>} network-y promise
 */
export declare function api(url: string | node_fetch.Request, init: node_fetch.RequestInit, suppressErrorReporting?: boolean): Promise<node_fetch.Response>;
