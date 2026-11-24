#!/usr/bin/env python3
"""Reproducible conformance tests for BOTERNITY's public promises (Python 3.8+, standard library only).

    python conformance/run.py                      # against https://boternity.com
    python conformance/run.py --site http://localhost:8000 --json

Each check is a public promise: the same tools on every interface (MCP, REST, OpenAPI, A2A), compact tool list, older
names still accepted, trust block on answers that state facts or scores, JSON-RPC errors per the MCP specification.
Only read-only tools are called. Exit code 0 when every check passes, 1 otherwise.
"""
import argparse
import json
from pathlib import Path
import sys
import time
import urllib.error
import urllib.request

HERE = Path(__file__).resolve().parent
TRUST_SCHEMA = json.loads((HERE.parent / "schemas" / "trust.schema.json").read_text(encoding="utf-8"))
UA = "boternity-conformance/1.0"
results = []


def fetch(url, body=None):
    headers = {"User-Agent": UA, "Accept": "application/json, text/event-stream"}
    data = None
    if body is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(body).encode()
    for attempt in range(4):  # fair-use limits: on HTTP 429, wait as asked (Retry-After) and retry
        request = urllib.request.Request(url, data=data, headers=headers, method="POST" if data else "GET")
        try:
            with urllib.request.urlopen(request, timeout=40) as response:
                return response.status, response.read().decode()
        except urllib.error.HTTPError as error:
            if error.code != 429 or attempt == 3:
                return error.code, error.read().decode()
            time.sleep(min(30, int(error.headers.get("Retry-After") or 10)))


def check(name, ok, detail=""):
    results.append({"check": name, "pass": bool(ok), "detail": "" if ok else str(detail)[:300]})


def valid(value, schema):
    """Small JSON Schema subset (type, required, properties, enum, minimum) — enough for the trust block."""
    types = schema.get("type")
    if types:
        kinds = {"object": dict, "array": list, "string": str, "integer": int, "null": type(None), "boolean": bool}
        allowed = types if isinstance(types, list) else [types]
        if not any(isinstance(value, kinds[t]) and not (t == "integer" and isinstance(value, bool)) for t in allowed):
            return False
    if "enum" in schema and value not in schema["enum"]:
        return False
    if isinstance(value, int) and "minimum" in schema and value < schema["minimum"]:
        return False
    if isinstance(value, dict):
        if any(k not in value for k in schema.get("required", [])):
            return False
        return all(valid(value[k], s) for k, s in schema.get("properties", {}).items() if k in value)
    if isinstance(value, list) and "items" in schema:
        return all(valid(v, schema["items"]) for v in value)
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--site", default="https://boternity.com")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    args = parser.parse_args()
    site = args.site.rstrip("/")
    api = site + "/api/public/v4"

    def rpc(method, params=None):
        code, text = fetch(api + "/mcp", {"jsonrpc": "2.0", "id": 1, "method": method, "params": params or {}})
        try:
            return code, json.loads(text)
        except ValueError:
            return code, {"http_status": code, "body": text[:200]}

    def tool(name, arguments):
        code, text = fetch(api + "/tools/" + name, arguments)
        return code, (json.loads(text).get("result") if code == 200 else text)

    code, init = rpc("initialize", {"protocolVersion": "2025-06-18", "capabilities": {},
                                    "clientInfo": {"name": "boternity-conformance", "version": "1.0"}})
    server = (init.get("result") or {}).get("serverInfo", {})
    check("MCP initialize answers with serverInfo and a protocol version",
          code == 200 and server.get("name") and init["result"].get("protocolVersion"), init)

    code, listed = rpc("tools/list")
    mcp_tools = (listed.get("result") or {}).get("tools", [])
    names = [t["name"] for t in mcp_tools]
    check("MCP tools/list returns tools", code == 200 and names, listed)
    check("every tool has an object outputSchema and MCP annotations",
          all(t.get("outputSchema", {}).get("type") == "object" and "readOnlyHint" in t.get("annotations", {})
              for t in mcp_tools), [t["name"] for t in mcp_tools if "annotations" not in t])
    tokens = len(json.dumps(listed.get("result", {}))) // 4
    check("tools/list costs at most 2,500 tokens of context (characters / 4)", tokens <= 2500, f"{tokens} tokens")

    code, text = fetch(api + "/tools")
    rest = [t["name"] for t in json.loads(text)["tools"]] if code == 200 else []
    check("REST GET /tools lists the same tools as MCP", rest == names, (rest, names))
    code, text = fetch(api + "/openapi.json")
    paths = [p.rsplit("/", 1)[1] for p in json.loads(text).get("paths", {}) if p.startswith("/tools/")] if code == 200 else []
    check("OpenAPI has one operation per listed tool", paths == names, (paths, names))
    code, text = fetch(site + "/.well-known/agent-card.json")
    skills = [s["id"] for s in json.loads(text).get("skills", [])] if code == 200 else []
    check("A2A agent card lists the same skills", skills == names, (skills, names))
    code, text = fetch(site + "/llms.txt")
    check("llms.txt describes every listed tool", code == 200 and all(f"- {n}: " in text for n in names),
          [n for n in names if f"- {n}: " not in text])

    code, out = tool("time", {"operation": "now", "timezone": "Europe/Paris"})
    check("REST call of a listed tool (time)", code == 200 and isinstance(out, dict), out)
    code, out = tool("get_current_time", {})
    check("an older tool name (get_current_time) is still accepted", code == 200 and isinstance(out, dict), out)
    code, out = tool("process_data", {"operation": "inspect_json", "data": "{\"a\": [1, 2]}", "pointer": "/a/1"})
    check("process_data inspect_json resolves an RFC 6901 pointer", code == 200 and isinstance(out, dict), out)

    for label, name, arguments in (("get_data earthquakes", "get_data", {"feed": "earthquakes"}),
                                   ("get_data feeds_status", "get_data", {"feed": "feeds_status"}),
                                   ("find_mcp_server github", "find_mcp_server", {"need": "github"}),
                                   ("find_mcp_server incidents", "find_mcp_server", {})):
        code, out = tool(name, arguments)
        block = out.get("trust") if isinstance(out, dict) else None
        check(f"{label}: trust block valid against schemas/trust.schema.json",
              code == 200 and block is not None and valid(block, TRUST_SCHEMA), block or out)
    code, out = tool("time", {"operation": "now"})
    check("answers that state no sourced fact carry no trust block (time)", isinstance(out, dict) and "trust" not in out)

    code, answer = rpc("no/such_method")
    check("unknown JSON-RPC method returns error -32601", (answer.get("error") or {}).get("code") == -32601, answer)
    code, answer = rpc("tools/call", {"name": "get_data", "arguments": {"feed": "nope"}})
    check("invalid tool arguments return a tool error (isError), not a crash",
          code == 200 and (answer.get("result") or {}).get("isError") is True, answer)

    failed = [r for r in results if not r["pass"]]
    if args.json:
        print(json.dumps({"site": site, "server": server, "passed": len(results) - len(failed), "failed": len(failed),
                          "checks": results}, indent=1))
    else:
        for r in results:
            print(("PASS  " if r["pass"] else "FAIL  ") + r["check"] + ("" if r["pass"] else "\n      " + r["detail"]))
        print(f"\n{len(results) - len(failed)}/{len(results)} checks passed against {site} "
              f"(server {server.get('version', '?')})")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
