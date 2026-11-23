# Changelog

All notable changes to the hosted BOTERNITY MCP server (`https://boternity.com/api/public/v4/mcp`).

## 23 November 2026

- New tool `check_site_for_agents`: can an AI agent get into a website, understand it and act on it? Grade A to F
  with concrete fixes, `robots.txt` read for 17 AI bots. Deterministic, at most 6 requests to the site, under the
  declared user agent `BOTERNITY-AgentCheck/1.0`. Also on the web: https://boternity.com/agent-check
- New tool `verify_ai_bot`: is that GPTBot, ClaudeBot or Googlebot really them? Checked only against the IP lists
  and reverse DNS methods the operators publish; bots with no published method are reported as unverifiable.
  Also on the web, with pasted access logs: https://boternity.com/bot-check
- 44 tools in total. Descriptions tightened so `tools/list` stays under its context budget.
- New monthly report, State of the agent web: 97 major websites tested by an honest, declared agent, open data
  (CC BY 4.0, CSV and JSON): https://boternity.com/reports/agent-web/2026-11
- New site navigation: every page in six sections, https://boternity.com/explore
- New "Suggest or ask" button on every page of boternity.com: send an idea, a tool request or a bug report straight
  to the team, e-mail optional. Requests for tools can still be opened as issues here.

## 22 November 2026 (website)

- Free down/up alerts for any server of the MCP Index: leave an e-mail (confirmed first) or an https webhook on the
  server page and get one message when it goes down and one when it is back. https://boternity.com/mcp-weather

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
