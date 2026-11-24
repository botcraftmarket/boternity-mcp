# MCP audit (test_mcp_server)

Run it: <https://boternity.com/mcp-audit> or MCP tool `test_mcp_server` (`url`, then `report_id` for the finished report).

Streamable HTTP tests from outside, like an MCP client: `initialize`, protocol version negotiation, session handling,
`notifications/initialized`, `tools/list` with a schema lint and its cost in tokens, `ping`, JSON-RPC error codes
(including `-32700` for invalid JSON), resources and prompts when the server announces them, CORS, `Origin` handling,
GET behaviour, latency (min, median, p90, max), and an optional real tool call (`probe_tool`).

**Score:** 100 minus 15 per failed check and 5 per warning. A server that cannot complete `initialize` and `tools/list`
is capped at 30. **Grades:** A from 90, B from 75, C from 60, D from 40, E below.

The report comes in JSON and Markdown and is kept 30 days (shareable link and README badge).

**Limits:** one run, from one location, at one moment. It tests protocol behaviour, not what the tools do.
