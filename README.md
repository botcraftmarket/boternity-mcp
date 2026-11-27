<!-- title:start -->
# BOTERNITY — Open infrastructure for AI agents

**Discover. Verify. Connect. Remember.**
<!-- title:end -->

[![MCP Index](https://boternity.com/mcp-index/badge.svg?name=com.boternity%2Fboternity)](https://boternity.com/mcp-index/server?name=com.boternity%2Fboternity)
[![BOTERNITY MCP connector](https://glama.ai/mcp/connectors/com.boternity/boternity/badges/score.svg)](https://glama.ai/mcp/connectors/com.boternity/boternity)
[![Indexed on TensorBlock MCP Index](https://mcp-index.tensorblock.co/v1/servers/github-botcraftmarket-boternity-mcp-1728ad22/badge.svg)](https://tensorblock.co/mcp/servers/github-botcraftmarket-boternity-mcp-1728ad22)
[![MCP Registry](https://img.shields.io/badge/MCP%20Registry-com.boternity%2Fboternity-38e1d0)](https://registry.modelcontextprotocol.io/v0/servers?search=com.boternity)
[![Tools](https://img.shields.io/badge/tools-9-38e1d0)](#tools-9)
[![No key](https://img.shields.io/badge/API%20key-not%20needed-2ea44f)](#connect)

<!-- positioning:start -->
Free, deterministic tools and open data that AI agents can call directly: no account, no key, no model behind the answers, and every score computed from real checks.

- **Discover.** Find what exists: every public remote MCP server checked every night, any web page read cleanly, fresh open data with its source and license. (`find_mcp_server`, `read_page`, `get_data`)
- **Verify.** Check before you trust: audit an MCP server out of 100, test a website the way an AI agent meets it, see which MCP servers are up right now. (`test_mcp_server`, `check_site_for_agents`)
- **Connect.** One set of tools through every door: MCP, REST, OpenAPI 3.1 and A2A, plus data and time utilities that make answers usable. (`process_data`, `time`)
- **Remember.** Keep state an agent cannot keep alone: a notebook that survives sessions, pages watched over days with diffs and webhooks. (`notebook`, `watch_page`)
<!-- positioning:end -->

- **No account, no API key, free.** Fair-use quotas; optional access keys for more.
- **Deterministic.** No model behind it; nothing you send is executed.
- **Every door.** MCP (Streamable HTTP), REST with OpenAPI 3.1, an A2A agent card, `llms.txt`, open JSON files.
- **Annotated.** Every tool carries MCP annotations (`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`).

The server is hosted: there is nothing to install. This repository holds the public documentation and metadata.

```
https://boternity.com/api/public/v4/mcp
```

## Connect

**Claude Code**

```bash
claude mcp add --transport http boternity https://boternity.com/api/public/v4/mcp
```

**Claude (claude.ai and desktop app)**: Settings → Connectors → Add custom connector, then paste the URL above.

**Cursor** (`~/.cursor/mcp.json`)

```json
{"mcpServers": {"boternity": {"url": "https://boternity.com/api/public/v4/mcp"}}}
```

**VS Code** (`.vscode/mcp.json`)

```json
{"servers": {"boternity": {"type": "http", "url": "https://boternity.com/api/public/v4/mcp"}}}
```

**ChatGPT custom GPT actions and API clients**: import `https://boternity.com/api/public/v4/openapi.json`.

**Plain HTTP** (every tool is also a REST call)

```bash
curl -X POST https://boternity.com/api/public/v4/tools/get_data \
  -H "Content-Type: application/json" -d '{"feed": "exchange_rates", "params": {"base": "EUR", "symbols": ["USD", "JPY"]}}'
```

**A2A (Agent2Agent)**: agent card at `https://boternity.com/.well-known/agent-card.json`, JSON-RPC endpoint
`https://boternity.com/api/public/v4/a2a` (`message/send` with a data part `{"skill": "read_page", "arguments": {...}}`).

Ready-made configs are in [`examples/`](examples).

<!-- capabilities:start -->
## Tools (9)

Server 3.0.0 lists **9 tools**, grouped by job, so loading the tool list stays under **2,500 tokens** of an agent's context. Every tool has MCP annotations and an `outputSchema`.

| Tool | What it does |
| --- | --- |
| `read_page` | Clean text of a public page (headings as Markdown), title, description, language, canonical URL, Open Graph, schema.org types, outline, links. robots.txt respected, cached, paginated. |
| `check_site_for_agents` | Can an AI agent get into a website, understand it and act on it? Grade A to F with fixes (bot walls, robots.txt read for 17 AI bots, text without JavaScript, schema.org, llms.txt, forms, APIs). |
| `watch_page` | Re-read a page on a schedule and keep diffs, changed sections and keyword events; part of a page (CSS selector), webhook on change. `action`: `start` (returns an id), then `get`, `check_now` or `stop` with that id. Useful because an agent cannot come back tomorrow on its own. |
| `test_mcp_server` | Full audit of a remote MCP server out of 100: version negotiation, sessions, tools/list lint and token cost, ping, error codes, CORS, latency, optional real tool call. Call again with `report_id` for the JSON and Markdown report. |
| `find_mcp_server` | The most reliable public MCP servers for a need (`{"need": "postgres"}`) from the nightly MCP Index; `server` for the live status of one server (up, slow, down); no argument for current incidents. |
| `get_data` | Fresh public data with its source, license and update time: `feed` + `params` (feeds listed below). |
| `notebook` | A private notebook per agent (secret token) that survives across sessions, 30 days after last use. `action`: `create`, `write`, `read`, `delete`. No personal data. |
| `process_data` | `operation`: `convert` (JSON, CSV, XML), `inspect_json` (validation with line and column, RFC 6901 pointer), `analyze_table` (per-column statistics), `clean_table`, `compare` (two tables by key, or two texts). |
| `time` | `operation`: `now` (any IANA timezone), `convert` (daylight saving aware), `duration`, `cron` (next runs). |

### `get_data` feeds

| `feed` | What it returns | Source, refresh |
| --- | --- | --- |
| `weather` | Current weather, 7-day forecast, air quality and local time for about 250 major cities | Open-Meteo |
| `exchange_rates` | Reference rates for about 30 currencies, today or any day of the last 90 days, any base | European Central Bank |
| `earthquakes` | Recent earthquakes worldwide, by magnitude, time window and distance from a point | USGS, every 10 min |
| `disaster_alerts` | Cyclones, floods, earthquakes, volcanoes, droughts, wildfires | GDACS (UN/EU) |
| `public_holidays` | Holidays of 200 countries; with a `date`: is it a business day, and the next one | Public holiday calendars |
| `trending_topics` | Most-read Wikipedia articles of the last full day, 16 languages | Wikimedia |
| `exploited_vulnerabilities` | CVEs exploited in the wild: one CVE, a vendor or product, or the newest | CISA KEV, every 6 h |
| `package_info` | Latest version, release date, license of the 500 most downloaded npm and PyPI packages | npm, PyPI |
| `service_status` | Official status of 26 services (GitHub, OpenAI, Anthropic, Cloudflare, Vercel, npm, Discord…) | Status pages |
| `ai_papers` | Newest arXiv papers in AI, ML, NLP, vision, robotics, agents, security, software engineering | arXiv |
| `hacker_news` | Front page, best, Ask HN or Show HN, with points and links | Hacker News, every 30 min |
| `key_numbers` | BOTERNITY's own citable numbers: health of every public MCP server, AI crawlers, MCP clients; each with date, method and permalink (`group` or `id`) | BOTERNITY measurements, CC BY 4.0, hourly |
| `feeds_status` | Freshness of every feed above (last update, stale or not) | BOTERNITY collectors |

Example: `{"feed": "weather", "params": {"city": "Paris"}}`. An unknown parameter is refused with the list of the parameters that feed accepts.

The server also exposes **MCP prompts** (`audit_mcp_server`, `watch_price`, `summarize_page`, `track_document_changes`, `compare_tables`, `remember_across_sessions`, `choose_mcp_server`, `is_mcp_server_up`, `agent_ready_site`, `mcp_ecosystem_numbers`) and **resources** (catalog extracts, `boternity://watch/{id}`, `boternity://mcp-test/{id}`).

### One set of tools, four ways in

One set of 9 tools (server 3.0.0), four ways in. Every way lists the same 9 names; older names are accepted everywhere but listed nowhere.

| Interface | Lists | Accepts |
| --- | --- | --- |
| MCP `https://boternity.com/api/public/v4/mcp` | `tools/list`: the 9 tools | `tools/call` with the 9 tools or an older name |
| REST | `GET https://boternity.com/api/public/v4/tools`: the 9 tools | `POST https://boternity.com/api/public/v4/tools/{name}` with the 9 tools or an older name |
| OpenAPI 3.1 `https://boternity.com/api/public/v4/openapi.json` | one operation per tool (9) | same as REST |
| A2A `https://boternity.com/.well-known/agent-card.json` | 9 skills, same names | data part `{"skill", "arguments"}`, the 9 names or an older name |

**Older tool names still work** (MCP `tools/call`, REST and A2A), they are just no longer listed: 60 names from versions 1.x and 2.x, for example `get_weather` → `get_data` with `feed: weather`, `create_notebook` → `notebook`, `convert_data` → `process_data`, `get_current_time` → `time`, `check_mcp_server_status` → `find_mcp_server`, `get_mcp_test` → `test_mcp_server`. Nothing breaks for an existing client. The full table, old name → tool that replaces it, is in `older_names` of `GET https://boternity.com/api/public/v4/capabilities`.
<!-- capabilities:end -->

## Try it

Once connected, ask your agent:

- *Is GitHub or OpenAI having an incident right now?*
- *What is 250 EUR in JPY at today's ECB rate, and is next Monday a business day in Japan?*
- *Find me a reliable MCP server for PostgreSQL, and check that it is up right now.*
- *Watch the pricing section of this page every 6 hours and tell me when "out of stock" appears.*
- *Audit my MCP server https://example.com/mcp and give me the three fixes that would raise its score the most.*
- *Create a BOTERNITY notebook for this project and save our decisions there after each session.*

More prompts on [boternity.com/examples](https://boternity.com/examples); where to start by profile on [boternity.com/guide](https://boternity.com/guide).

## BOTERNITY MCP Index

Every night, BOTERNITY checks every public remote MCP server of the official MCP Registry (over 13,000 entries) like a real
client, and scores it out of 100 on reliability, protocol conformance, tool definitions and context cost. No tool is ever called.

- [Ranking](https://boternity.com/mcp-index) and [best servers by category](https://boternity.com/mcp-index/best) (PostgreSQL, GitHub, web search, e-mail…)
- [MCP weather](https://boternity.com/mcp-weather): which servers are down, unstable or slow right now ([incidents feed](https://boternity.com/mcp-weather/incidents.xml))
- [Monthly report: State of remote MCP servers](https://boternity.com/reports)
- [Scoring method](https://boternity.com/mcp-index/method) · [Free full audit](https://boternity.com/mcp-audit)

**Run an MCP server?** [Claim your badge](https://boternity.com/mcp-index/claim): a score badge for your README that updates by
itself, plus a live status badge:

```markdown
[![MCP Index](https://boternity.com/mcp-index/badge.svg?name=<registry name>)](https://boternity.com/mcp-index/server?name=<registry name>)
```

## Open data

Free, with CORS:

- [`/mcp-index/data.json`](https://boternity.com/mcp-index/data.json): the whole MCP Index (filters `topic`, `status`, `min_score`, `q`), CC BY 4.0
- [`/mcp-weather.json`](https://boternity.com/mcp-weather.json): live state of watched MCP servers, every 10 minutes
- [`/observatory.json`](https://boternity.com/observatory.json): aggregated activity (MCP connections, AI crawlers, most used tools), CC BY 4.0
- [`/data`](https://boternity.com/data): every fresh dataset as an open file, under the license of its source
- [`/ai-crawlers.json`](https://boternity.com/ai-crawlers.json) and [`/mcp-builders.json`](https://boternity.com/mcp-builders.json): weekly AI crawler trends, MCP client behaviour and common server problems

See also the [Observatory](https://boternity.com/observatory), [which AI crawlers read the web](https://boternity.com/ai-crawlers)
and the [public log](https://boternity.com/journal) of what changes on BOTERNITY each day.

## Trust

Answers that state a fact or a score (`get_data`, `find_mcp_server`, `check_site_for_agents`, `test_mcp_server`,
`read_page`) carry a `trust` block: source, `observed_at`, `verified_at`, `verification_method`, `freshness_seconds`,
`data_status`, `limitations`. Every score comes from a published, deterministic method: no AI model on the data, no paid
ranking, no invented numbers. Methods, error reports and the dated history of every method change:
https://boternity.com/trust

## In this repository

| Folder | What |
| --- | --- |
| [`clients/`](clients/) | Official clients, one file each, no dependency: Python 3.8+ and JavaScript (Node 18+, browsers) |
| [`schemas/`](schemas/) | JSON Schemas generated from the server code: every tool, and the trust block |
| [`methodology/`](methodology/) | How each score and dataset is produced: MCP Index, agent-ready score, MCP audit, MCP weather, data feeds |
| [`conformance/`](conformance/) | `python conformance/run.py`: reproducible checks of our public promises against the live service |
| [`examples/`](examples/) | Client configurations, `curl` calls and real responses captured from the live service (`examples/responses/`) |

## Security and privacy

- Inputs are not stored, except a watched page's text, a notebook's notes and an MCP audit report, all temporary. Do not send personal data. Details: [privacy policy](https://boternity.com/privacy).
- Outgoing requests (page reading, watching, audits) run in an isolated worker that cannot reach private or local networks; every redirect is re-checked.
- No cookies, no tracking of individual users; client IP addresses are not stored by the gateway.

## Support

Open an [issue](https://github.com/botcraftmarket/boternity-mcp/issues) · [support page](https://boternity.com/support) · [terms](https://boternity.com/terms)

## Links

- Website: https://boternity.com · Guide: https://boternity.com/guide
- MCP endpoint: https://boternity.com/api/public/v4/mcp
- OpenAPI: https://boternity.com/api/public/v4/openapi.json
- A2A agent card: https://boternity.com/.well-known/agent-card.json
- For agents: https://boternity.com/llms.txt
- Official MCP Registry: `com.boternity/boternity`
