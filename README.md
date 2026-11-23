# BOTERNITY · free remote MCP server for AI agents

[![MCP Index](https://boternity.com/mcp-index/badge.svg?name=com.boternity%2Fboternity)](https://boternity.com/mcp-index/server?name=com.boternity%2Fboternity)
[![BOTERNITY MCP connector](https://glama.ai/mcp/connectors/com.boternity/boternity/badges/score.svg)](https://glama.ai/mcp/connectors/com.boternity/boternity)
[![Indexed on TensorBlock MCP Index](https://mcp-index.tensorblock.co/v1/servers/github-botcraftmarket-boternity-mcp-1728ad22/badge.svg)](https://tensorblock.co/mcp/servers/github-botcraftmarket-boternity-mcp-1728ad22)
[![MCP Registry](https://img.shields.io/badge/MCP%20Registry-com.boternity%2Fboternity-38e1d0)](https://registry.modelcontextprotocol.io/v0/servers?search=com.boternity)
[![Tools](https://img.shields.io/badge/tools-42-38e1d0)](#tools-42)
[![No key](https://img.shields.io/badge/API%20key-not%20needed-2ea44f)](#connect)

BOTERNITY gives AI agents what they cannot do alone: **fresh public data with its source** (weather, exchange rates,
earthquakes, holidays, CVEs, service status, packages, papers), **web pages read cleanly and watched over days**,
**MCP servers audited and ranked**, data tools and **memory across sessions**.

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
curl -X POST https://boternity.com/api/public/v4/tools/get_exchange_rates \
  -H "Content-Type: application/json" -d '{"base": "EUR", "symbols": ["USD", "JPY"]}'
```

**A2A (Agent2Agent)**: agent card at `https://boternity.com/.well-known/agent-card.json`, JSON-RPC endpoint
`https://boternity.com/api/public/v4/a2a` (`message/send` with a data part `{"skill": "read_page", "arguments": {...}}`).

Ready-made configs are in [`examples/`](examples).

## Tools (42)

### Fresh public data (11)

Collected and refreshed by BOTERNITY; every answer says where the data comes from, its license and when it was last updated.

| Tool | What it returns | Source, refresh |
| --- | --- | --- |
| `get_weather` | Current weather, 7-day forecast, air quality and local time for about 250 major cities | Open-Meteo |
| `get_exchange_rates` | Reference rates for about 30 currencies, today or any day of the last 90 days, any base | European Central Bank |
| `get_earthquakes` | Recent earthquakes worldwide, by magnitude, time window and distance from a point | USGS, every 10 min |
| `get_disaster_alerts` | Cyclones, floods, earthquakes, volcanoes, droughts, wildfires | GDACS (UN/EU) |
| `get_public_holidays` | Holidays of 200 countries; with a date: is it a business day, and the next one | Public holiday calendars |
| `get_trending_topics` | Most-read Wikipedia articles of the last full day, 16 languages | Wikimedia |
| `get_exploited_vulnerabilities` | CVEs exploited in the wild: one CVE, a vendor or product, or the newest | CISA KEV, every 6 h |
| `get_package_info` | Latest version, release date, license of the 500 most downloaded npm and PyPI packages | npm, PyPI |
| `get_service_status` | Official status of 26 services (GitHub, OpenAI, Anthropic, Cloudflare, Vercel, npm, Discord…) | Status pages |
| `get_new_ai_papers` | Newest arXiv papers in AI, ML, NLP, vision, robotics, agents, security, software engineering | arXiv |
| `get_hacker_news` | Front page, best, Ask HN or Show HN, with points and links | Hacker News, every 30 min |

### MCP ecosystem (4)

| Tool | What it does |
| --- | --- |
| `find_mcp_server` | The most reliable public MCP servers for a need (`{"need": "postgres"}`), with endpoint and score, from the nightly MCP Index. |
| `check_mcp_server_status` | Live MCP weather: is a public MCP server up, down, unstable or slow right now? |
| `test_mcp_server`, `get_mcp_test` | Full audit of a remote MCP server out of 100: initialize, version negotiation, sessions, tools/list lint and token cost, ping, error codes, CORS, Origin, latency, optional real tool call. JSON and Markdown report. |

### Web pages (5)

| Tool | What it does |
| --- | --- |
| `read_page` | Clean text (headings as Markdown), title, description, language, canonical URL, Open Graph, schema.org types, outline, links. robots.txt respected, cached, paginated. |
| `watch_page`, `get_watch`, `check_watch_now`, `stop_watch` | Re-read a page on a schedule and keep diffs, changed sections and keyword events. Watch part of a page (CSS selector), get a webhook POST on change. |

### Memory (4)

`create_notebook`, `write_note`, `read_notes`, `delete_note`: a private notebook per agent (secret token) that survives
across sessions, for 30 days after last use.

### Data (6)

`convert_data` (JSON ⇄ CSV ⇄ XML), `inspect_json` (validation, RFC 6901 pointers), `analyze_table` (per-column statistics),
`compare_tables` (rows added, removed, changed by key), `clean_table`, `compare_texts` (unified diff).

### Time (4)

`get_current_time`, `convert_time` (IANA timezones, daylight saving time), `compute_duration`, `list_cron_runs`.

### Utilities (4)

`encode_text` (Base64, URL, hashes), `generate_uuid`, `parse_url`, `explain_http_status` (reason phrase, specification, retry guidance).

### Catalog and requests (4)

`search_catalog`, `read_catalog_resource` (verified extracts of specifications), `request_resource` and
`get_request_status` (ask for a tool or a resource you are missing: requests shape what gets built next).

The server also exposes **MCP prompts** (`audit_mcp_server`, `watch_price`, `summarize_page`, `track_document_changes`,
`compare_tables`, `remember_across_sessions`) and **resources** (catalog extracts, `boternity://watch/{id}`,
`boternity://mcp-test/{id}`).

**Older tool names still work**, they are just no longer listed: names from versions 1.x (`current_time`, `json_to_csv`,
`data_stats`…), `check_business_day` (now `get_public_holidays` with a `date`), and `get_data_feeds_status` (now the open file
[`/data/status.json`](https://boternity.com/data/status.json)).

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
