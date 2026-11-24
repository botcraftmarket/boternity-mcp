# Methodology

How BOTERNITY measures, scores and sources what it publishes. Every score is computed by a deterministic program (no AI
model, no manual adjustment, no paid placement) from real checks. The canonical, always-current version of each method is
its page on boternity.com; these files are copies updated with every method change.

| Method | What it produces | Canonical page |
| --- | --- | --- |
| [MCP Index score](mcp-index.md) | Score /100 and grade A–E of every public remote MCP server, every night | <https://boternity.com/mcp-index/method> |
| [Agent-ready score](agent-ready.md) | Score /100 and grade A–F: can an AI agent get into a website, understand it and act on it? | <https://boternity.com/agent-check/method> |
| [MCP audit](mcp-audit.md) | About 30 protocol checks of one MCP server, on demand | <https://boternity.com/mcp-audit> |
| [MCP weather](mcp-weather.md) | Live up / unstable / slow / down state of about 190 MCP servers | <https://boternity.com/mcp-weather> |
| [Open data feeds](data-feeds.md) | Fresh public data with its source and license | <https://boternity.com/data> |
| [Trust block](trust-block.md) | `trust` object in answers: source, dates, method, freshness, limitations | <https://boternity.com/trust> |

**Changes.** Every method change and every confirmed correction is dated in
[/trust/history.json](https://boternity.com/trust/history.json) (CC BY 4.0) and shown on <https://boternity.com/trust>.

**Found an error?** Report it on <https://boternity.com/trust#report>, or open an issue in this repository.

**Reproduce.** [`conformance/run.py`](../conformance/run.py) checks BOTERNITY's own public promises against the live
service; the MCP audit can be run on any server at <https://boternity.com/mcp-audit>.
