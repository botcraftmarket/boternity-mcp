# MCP Index score (scoring version 3, since 22 November 2026)

Canonical page: <https://boternity.com/mcp-index/method>

Every night, each public remote MCP server of the [official MCP registry](https://registry.modelcontextprotocol.io) gets
the same short check, from an isolated worker, one request at a time per host, identified as `BOTERNITY-MCP-Index`:
`initialize`, `notifications/initialized`, `tools/list`, `ping` and one unknown method (to see how errors are handled).
**No tool is ever called.**

## Score out of 100

| Part | Points | What earns them |
| --- | --- | --- |
| Reliability | 30 | 10 for a valid `initialize`, 5 for a correct `ping`, up to 15 for speed (median ≤ 200 ms: 15, ≤ 500 ms: 11, ≤ 1 s: 7, ≤ 2 s: 3). Minus 5 if `tools/list` fails. |
| Protocol conformance | 20 | 8 for the current protocol revision (4 for 2025-03-26, 1 for 2024-11-05), 2 for `serverInfo.name`, 1 for `serverInfo.version`, 2 for server instructions, 2 for a well-formed JSON-RPC response, 5 when an unknown method returns JSON-RPC error `-32601` (3 for another error code). |
| Tool definitions | 40 | Average quality of every tool, out of 1: description of 40 to 1000 characters 0.25, parameters documented 0.20 and typed 0.15 (0.35 when the tool takes none), `readOnlyHint` or `destructiveHint` 0.15, `idempotentHint` and `openWorldHint` 0.05, a `title` 0.05, an `outputSchema` 0.15. Duplicate tool names halve this part. |
| Context cost | 10 | Tokens that `tools/list` adds to every agent's context: ≤ 2,500: 10, ≤ 6,000: 7, ≤ 12,000: 4, ≤ 20,000: 2. |

**Grades:** A from 90, B from 75, C from 60, D from 40, E below. Servers that require sign-in before `initialize` are listed
but not scored. Scores made with an older scoring version are not ranked until the server's next nightly check.

## Topics

A server belongs to a topic (PostgreSQL, GitHub, web search…) only if the keyword is in its name, its title or the first
sentence of its description. Within a topic: healthy servers first, servers built for the need before those that only
mention it, then score, then 30-day availability, then latency.

## Limits

One check per night, from one location (Europe). A server can change between checks. The score measures protocol
behaviour and tool definitions, not the quality or safety of what the tools do. Scores are automatic and can be wrong:
owners can ask for a re-check or removal via <https://boternity.com/support>.

## Open data

The whole index: <https://boternity.com/mcp-index/data.json> (filters `topic`, `status`, `min_score`, `q`; CC BY 4.0).
Agents: MCP tool `find_mcp_server` on `https://boternity.com/api/public/v4/mcp`.
