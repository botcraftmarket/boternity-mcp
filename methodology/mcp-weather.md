# MCP weather

Live page: <https://boternity.com/mcp-weather> · JSON: <https://boternity.com/mcp-weather.json> (CC BY 4.0)

**Which servers.** The 5 best healthy servers of each topic of the MCP Index, the 60 best rated overall, and servers that
visitors asked to monitor ("monitoring wanted"), if they are in the index with an endpoint: about 190 servers.

**How.** One MCP `initialize` request per server, about every 20 minutes (at most 120 checks every 10 minutes), one host
at a time, identified as `BOTERNITY-MCP-Weather`. No tool is ever called.

**States.**

| State | Rule |
| --- | --- |
| up | The last check answered normally. |
| unstable | The last check failed once. |
| down | 2 failed checks in a row. |
| slow | Answering, but at least 3 times its usual latency, at least 1 s slower and at least 1.5 s. |

Incidents are kept 7 days (Atom feed: <https://boternity.com/mcp-weather/incidents.xml>).

**Limits.** About 190 servers only; every other server is checked once a night by the MCP Index. Answering `initialize`
does not prove every tool works.

Agents: MCP tool `find_mcp_server` with `server` (one server), `need` + `up_now` (servers up right now for a need), or no
argument (current incidents).
