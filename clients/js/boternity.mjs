// Official BOTERNITY client for JavaScript (Node 18+, Deno, Bun and browsers: uses fetch, no dependency). License: MIT.
//
//   import { Boternity, isFresh } from "./boternity.mjs";
//   const bt = new Boternity();
//   const quake = await bt.getData("earthquakes", { min_magnitude: 5 });
//   console.log(quake.data[0], quake.trust.data_status);
//
// Every call goes to the public REST API (https://boternity.com/api/public/v4), which runs the same 9 tools as the MCP
// server. No key is needed; an optional access key (btk_...) raises quotas.

export const VERSION = "1.0.0";
export const BASE = "https://boternity.com/api/public/v4";
const PENDING = new Set(["queued", "running", "pending"]);
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

export class BoternityError extends Error {
  constructor(status, detail) {
    super(`HTTP ${status}: ${detail}`);
    this.status = status;
    this.detail = detail;
  }
}

export class Boternity {
  constructor({ base = BASE, key = null, timeoutMs = 30000 } = {}) {
    this.base = base.replace(/\/$/, "");
    this.key = key;
    this.timeoutMs = timeoutMs;
  }

  async request(path, body) {
    const headers = { Accept: "application/json" };
    if (body !== undefined) headers["Content-Type"] = "application/json";
    if (this.key) headers.Authorization = `Bearer ${this.key}`;
    const response = await fetch(this.base + path, {
      method: body === undefined ? "GET" : "POST",
      headers,
      body: body === undefined ? undefined : JSON.stringify(body),
      signal: AbortSignal.timeout(this.timeoutMs),
    });
    const data = await response.json().catch(() => ({}));
    if (!response.ok) throw new BoternityError(response.status, data.detail ?? response.statusText);
    return data;
  }

  // Generic
  async tools() { return (await this.request("/tools")).tools; }
  async call(tool, args = {}) { return (await this.request(`/tools/${tool}`, args)).result; }
  async mcp(method, params = {}, id = 1) { return this.request("/mcp", { jsonrpc: "2.0", id, method, params }); }

  // The 9 tools
  readPage(url, options = {}) { return this.call("read_page", { url, ...options }); }

  async checkSiteForAgents(url, { waitMs = 60000 } = {}) {
    const deadline = Date.now() + waitMs;
    for (;;) {
      const result = await this.call("check_site_for_agents", { url });
      if (!PENDING.has(result.status) || Date.now() > deadline) return result;
      await sleep(3000);
    }
  }

  async testMcpServer(url, { probeTool, waitMs = 90000 } = {}) {
    let job = await this.call("test_mcp_server", probeTool ? { url, probe_tool: probeTool } : { url });
    const deadline = Date.now() + waitMs;
    while (PENDING.has(job.status) && job.id && Date.now() < deadline) {
      await sleep(3000);
      job = await this.call("test_mcp_server", { report_id: job.id });
    }
    return job;
  }

  findMcpServer({ need, server, ...options } = {}) {
    const args = { ...options };
    if (need !== undefined) args.need = need;
    if (server !== undefined) args.server = server;
    return this.call("find_mcp_server", args);
  }

  getData(feed, params) { return this.call("get_data", params ? { feed, params } : { feed }); }
  watchPage(action = "start", options = {}) { return this.call("watch_page", { action, ...options }); }
  notebook(action, options = {}) { return this.call("notebook", { action, ...options }); }
  processData(operation, options = {}) { return this.call("process_data", { operation, ...options }); }
  time(operation = "now", options = {}) { return this.call("time", { operation, ...options }); }
}

// Trust helpers: the trust block of an answer, and whether it is recent enough to act on.
export const trust = (result) => (result && typeof result === "object" ? result.trust ?? null : null);

export function isFresh(result, maxAgeSeconds) {
  const block = trust(result);
  return Boolean(block) && !["stale", "unavailable", "pending"].includes(block.data_status)
    && block.freshness_seconds != null && block.freshness_seconds <= maxAgeSeconds;
}
