# Changelog

All notable changes to the hosted BOTERNITY MCP server (`https://boternity.com/api/public/v4/mcp`).

## 24 November 2026: one source for every description of the server

- `llms.txt`, `/api/discovery`, `/api/public/v4/capabilities`, the A2A agent card, the website pages and this README are now
  generated from the server's own code, and a test fails if any of them disagrees with `tools/list`. Fixed on the way:
  `llms.txt` still presented the 11 old data tool names as MCP tools and said the catalog may be empty;
  `/capabilities` listed 48 internal names instead of the 9 tools.
- `GET /api/public/v4/capabilities` now gives `server_version` and `older_names.replaced_by`: every 1.x and 2.x tool name
  with the 3.0.0 tool that replaces it (for example `get_weather` → `get_data` with `feed: weather`). Older names still work.
- No change to the tools themselves or to their schemas.

## 24 November 2026: server 3.0.0, 9 tools

- The MCP server lists **9 tools instead of 44**, with the same features: `read_page`, `check_site_for_agents`,
  `watch_page`, `test_mcp_server`, `find_mcp_server`, `get_data` (all 11 data feeds), `notebook`, `process_data`,
  `time`. Loading the tool list now costs about 2,300 tokens of an agent's context instead of 5,900: our own
  measure of 6,500 public MCP servers found that the number of tools drives most of that cost
  (https://boternity.com/reports/state-of-mcp-servers/2026-11#where-the-tokens-go).
- Every tool now declares an `outputSchema`.
- All older tool names (2.x and 1.x) still work over MCP, REST and A2A; they are just no longer listed.

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
- Agent-ready leaderboard: the monthly panel plus sites whose owners opt in, re-tested weekly, with up / down /
  stable arrows and an embeddable badge. A site can leave it with `boternity-leaderboard: no` in its `robots.txt`
  or `llms.txt`. https://boternity.com/agent-check/leaderboard
- Stricter agent-ready scoring (v2), also returned by `check_site_for_agents` (`scoring_version: 2`): the grade
  now counts points earned out of 100: getting in (30), being understood (35), offering ways to act (35: MCP
  server, OpenAPI description, A2A agent card, structured offers). 100 means perfect on every criterion. Every
  listed site has a public page with its points per criterion and how to gain the missing ones:
  https://boternity.com/agent-check/method
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
