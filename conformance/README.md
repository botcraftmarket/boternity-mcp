# Conformance tests

`run.py` checks BOTERNITY's public promises against the live service, with Python 3.8+ and nothing to install:

```bash
python conformance/run.py            # human-readable
python conformance/run.py --json     # machine-readable
```

What it checks (read-only tools only):

- the same tools on every interface: MCP `tools/list`, REST `GET /tools`, OpenAPI operations, A2A agent card skills,
  llms.txt;
- every tool has an object `outputSchema` and MCP annotations; `tools/list` costs at most 2,500 tokens;
- an older tool name (`get_current_time`) is still accepted (backward compatibility);
- answers of `get_data` and `find_mcp_server` carry a trust block valid against
  [`schemas/trust.schema.json`](../schemas/trust.schema.json), and answers without sourced facts carry none;
- JSON-RPC errors: an unknown method returns `-32601`; bad tool arguments return a tool error (`isError`).

Exit code 0 when everything passes. If a check fails, please open an issue with the output.
