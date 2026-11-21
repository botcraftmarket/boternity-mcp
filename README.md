# BOTERNITY · free remote MCP server for AI agents

[![MCP score](https://boternity.com/api/public/v4/badge/4e19c3ab379a52016d4aedd7.svg)](https://boternity.com/mcp-audit?report=4e19c3ab379a52016d4aedd7)
[![BOTERNITY MCP connector](https://glama.ai/mcp/connectors/com.boternity/boternity/badges/score.svg)](https://glama.ai/mcp/connectors/com.boternity/boternity)
[![MCP Registry](https://img.shields.io/badge/MCP%20Registry-com.boternity%2Fboternity-38e1d0)](https://registry.modelcontextprotocol.io/v0/servers?search=com.boternity)

BOTERNITY gives AI agents what they cannot do alone: **read any web page cleanly, watch pages for changes over days, audit MCP servers, transform data and keep notes across sessions.**

- **No account, no API key, free** (fair-use quotas; optional access keys for more).
- **Deterministic**: no model behind it, nothing you send is executed.
- **Every door**: MCP (Streamable HTTP), REST with OpenAPI 3.1, A2A agent card, `llms.txt`.
- **Safe by design**: every tool carries MCP annotations (`readOnlyHint`, `destructiveHint`), so clients know which ones only read.

This repository holds the public documentation and metadata. The server is hosted: there is nothing to install.

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

**Plain HTTP**

```bash
curl -X POST https://boternity.com/api/public/v4/tools/read_page \
  -H "Content-Type: application/json" -d '{"url": "https://example.com"}'
```

**A2A (Agent2Agent)**: agent card at `https://boternity.com/.well-known/agent-card.json`, JSON-RPC endpoint `https://boternity.com/api/public/v4/a2a` (`message/send` with a data part `{"skill": "read_page", "arguments": {...}}`).

## Tools (29)

| Area | Tools | What it does |
| --- | --- | --- |
| Web pages | `read_page` | Clean text (headings as Markdown), title, description, language, canonical URL, Open Graph, schema.org types, outline, links. robots.txt respected, 10-minute cache, pagination. |
| Page watching | `watch_page`, `get_watch`, `check_watch_now`, `stop_watch` | Re-reads a page on a schedule and keeps diffs, changed sections and keyword events. Watch only part of a page (CSS selector), get a webhook POST on change. |
| MCP audit | `test_mcp_server`, `get_mcp_test` | Scores a remote MCP server out of 100: initialize, version negotiation, sessions, tools/list schema lint and token cost, ping, error codes, resources, prompts, CORS, Origin, latency, optional real tool call. JSON and Markdown report. |
| Memory | `create_notebook`, `write_note`, `read_notes`, `delete_note` | A private notebook per agent (secret token) that survives across sessions, for 30 days after last use. |
| Data | `convert_data`, `inspect_json`, `analyze_table`, `compare_tables`, `clean_table`, `compare_texts` | JSON ⇄ CSV ⇄ XML, validation and RFC 6901 pointers, per-column statistics, table comparison by key, cleaning, text diffs. |
| Time | `get_current_time`, `convert_time`, `compute_duration`, `list_cron_runs` | Present moment, IANA timezones with daylight saving time, durations, next cron runs. |
| Utilities | `encode_text`, `generate_uuid`, `parse_url`, `explain_http_status` | Base64 and URL encoding, hashes, UUIDs, URL parsing, HTTP status codes with retry guidance. |
| Catalog | `search_catalog`, `read_catalog_resource`, `request_resource`, `get_request_status` | Verified extracts of specifications (MCP, HTTP, OpenAPI, robots.txt); ask for what you need. |

Names from versions 1.x (`current_time`, `json_to_csv`, `data_stats`, `note_put`…) still work.

The server also exposes **MCP prompts** (`audit_mcp_server`, `watch_price`, `summarize_page`, `track_document_changes`, `compare_tables`, `remember_across_sessions`) and **resources** (catalog extracts, `boternity://watch/{id}`, `boternity://mcp-test/{id}`).

## Try it

Ask your agent, once connected:

- *Use BOTERNITY to read https://www.rfc-editor.org/rfc/rfc9110.html and summarize it.*
- *With BOTERNITY, watch the price block of this product page every 6 hours and track "out of stock".*
- *Audit my MCP server https://example.com/mcp with BOTERNITY and give me the three most important fixes.*
- *Create a BOTERNITY notebook for this project and save our decisions there after each session.*

More on [boternity.com/examples](https://boternity.com/examples). Audit your own MCP server for free at [boternity.com/mcp-audit](https://boternity.com/mcp-audit) and add your score badge to your README.

## Security and privacy

- Inputs are not stored, except a watched page's text, a notebook's notes and an MCP audit report, all temporary. Do not send personal data. Full details: [privacy policy](https://boternity.com/privacy).
- Outgoing requests (page reading, watching, audits) run in an isolated worker that cannot reach private or local networks; every redirect is re-checked.
- No cookies, no tracking of individual users; client IP addresses are not stored by the gateway.

## Support

Open an [issue](https://github.com/botcraftmarket/boternity-mcp/issues) · [support page](https://boternity.com/support) · [terms](https://boternity.com/terms)

## Links

- Website: https://boternity.com
- MCP endpoint: https://boternity.com/api/public/v4/mcp
- OpenAPI: https://boternity.com/api/public/v4/openapi.json
- A2A agent card: https://boternity.com/.well-known/agent-card.json
- For agents: https://boternity.com/llms.txt
- Official MCP Registry: `com.boternity/boternity`
