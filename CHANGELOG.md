# Changelog

All notable changes to the hosted BOTERNITY MCP server (`https://boternity.com/api/public/v4/mcp`).

## 2.2.1 · 22 November 2026

- Lighter tool definitions: shorter descriptions and schemas, so `tools/list` costs agents less context. Same 42 tools, same names.
- `serverInfo.version` now reports the real version.
- Reminder: `check_business_day` is served by `get_public_holidays` with a `date`, and `get_data_feeds_status` by
  `https://boternity.com/data/status.json`; both old names are still accepted.

## 2.2.0 · 22 November 2026

- New fresh-data tools: `get_package_info` (500 most downloaded npm and PyPI packages), `get_service_status`
  (26 services), `get_new_ai_papers` (arXiv), `get_hacker_news`; air quality and local time in `get_weather`;
  business-day check in `get_public_holidays`.
- `check_mcp_server_status`: live MCP weather (up, down, unstable, slow) for public MCP servers.
- 42 tools in total.

## 2.1.0 · 22 November 2026

- Fresh public data with source and license in every answer: `get_weather`, `get_exchange_rates` (ECB),
  `get_earthquakes` (USGS), `get_disaster_alerts` (GDACS), `get_public_holidays`, `get_trending_topics` (Wikipedia),
  `get_exploited_vulnerabilities` (CISA KEV).
- `find_mcp_server`: the most reliable public MCP servers for a need, from the nightly MCP Index.

## 2.0.0 · 21 November 2026

- Tools renamed to consistent `verb_noun` names and grouped (29 tools); MCP annotations on every tool.
  Names from 1.x keep working.
- Privacy, terms and support pages.

## 1.4.0 · 21 November 2026

- MCP prompts, dynamic resources, OpenAPI 3.1 description, A2A agent card, persistent notebooks.

## 1.3.0 · 21 November 2026

- `read_page`, page watching v2 (CSS selector, keywords, webhook), MCP server tester v2 (score out of 100).

## 1.0.0 · 21 November 2026

- First public release: deterministic tools for agents over MCP (Streamable HTTP), no sign-in.
