"""Official BOTERNITY client for Python 3.8+ (standard library only, one file).

    from boternity import Boternity
    bt = Boternity()
    quake = bt.get_data("earthquakes", min_magnitude=5)
    print(quake["data"][0], quake["trust"]["data_status"])

Every call goes to the public REST API (https://boternity.com/api/public/v4), which runs the same 9 tools as the MCP
server. No key is needed; an optional access key (btk_...) raises quotas. License: MIT.
"""
import json
import time
import urllib.error
import urllib.request

__version__ = "1.0.0"
BASE = "https://boternity.com/api/public/v4"
PENDING = ("queued", "running", "pending")


class BoternityError(Exception):
    """HTTP error from the API: .status (int) and .detail (message from the server)."""

    def __init__(self, status, detail):
        super().__init__(f"HTTP {status}: {detail}")
        self.status, self.detail = status, detail


class Boternity:
    def __init__(self, base=BASE, key=None, timeout=30, user_agent=None):
        self.base, self.key, self.timeout = base.rstrip("/"), key, timeout
        self.user_agent = user_agent or f"boternity-python/{__version__}"

    # --- transport -------------------------------------------------------------------------------------------------
    def _request(self, path, body=None):
        headers = {"User-Agent": self.user_agent, "Accept": "application/json"}
        data = None
        if body is not None:
            headers["Content-Type"] = "application/json"
            data = json.dumps(body).encode()
        if self.key:
            headers["Authorization"] = "Bearer " + self.key
        request = urllib.request.Request(self.base + path, data=data, headers=headers, method="POST" if data else "GET")
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                return json.loads(response.read().decode())
        except urllib.error.HTTPError as error:
            try:
                detail = json.loads(error.read().decode()).get("detail")
            except ValueError:
                detail = error.reason
            raise BoternityError(error.code, detail) from None

    # --- generic ---------------------------------------------------------------------------------------------------
    def tools(self):
        """The listed tools with their JSON Schemas (same list as MCP tools/list)."""
        return self._request("/tools")["tools"]

    def call(self, tool, arguments=None):
        """Call one tool; returns its result object (with a "trust" block when the answer states facts or scores)."""
        return self._request("/tools/" + tool, arguments or {})["result"]

    def mcp(self, method, params=None, ident=1):
        """Raw JSON-RPC call to the MCP endpoint (Streamable HTTP, JSON responses, no session needed)."""
        return self._request("/mcp", {"jsonrpc": "2.0", "id": ident, "method": method, "params": params or {}})

    # --- the 9 tools -----------------------------------------------------------------------------------------------
    def read_page(self, url, **options):
        return self.call("read_page", {"url": url, **options})

    def check_site_for_agents(self, url, wait=60):
        """Grade A-F of a site for AI agents; waits for the result (polls every 3 s, up to `wait` seconds)."""
        deadline = time.time() + wait
        while True:
            result = self.call("check_site_for_agents", {"url": url})
            if result.get("status") not in PENDING or time.time() > deadline:
                return result
            time.sleep(3)

    def test_mcp_server(self, url, probe_tool=None, wait=90):
        """Audit a remote MCP server out of 100; waits for the report (polls every 3 s, up to `wait` seconds)."""
        job = self.call("test_mcp_server", {"url": url, **({"probe_tool": probe_tool} if probe_tool else {})})
        deadline = time.time() + wait
        while job.get("status") in PENDING and job.get("id") and time.time() < deadline:
            time.sleep(3)
            job = self.call("test_mcp_server", {"report_id": job["id"]})
        return job

    def find_mcp_server(self, need=None, server=None, **options):
        args = {k: v for k, v in (("need", need), ("server", server)) if v is not None}
        return self.call("find_mcp_server", {**args, **options})

    def get_data(self, feed, **params):
        return self.call("get_data", {"feed": feed, "params": params} if params else {"feed": feed})

    def watch_page(self, action="start", **options):
        return self.call("watch_page", {"action": action, **options})

    def notebook(self, action, **options):
        return self.call("notebook", {"action": action, **options})

    def process_data(self, operation, **options):
        return self.call("process_data", {"operation": operation, **options})

    def time(self, operation="now", **options):
        return self.call("time", {"operation": operation, **options})


# --- trust helpers -------------------------------------------------------------------------------------------------
def trust(result):
    """The trust block of an answer (source, observed_at, verified_at, freshness_seconds, data_status...), or None."""
    return result.get("trust") if isinstance(result, dict) else None


def is_fresh(result, max_age_seconds):
    """True when the answer has a trust block, is not stale or unavailable, and is at most max_age_seconds old."""
    block = trust(result)
    return bool(block) and block.get("data_status") not in ("stale", "unavailable", "pending") \
        and block.get("freshness_seconds") is not None and block["freshness_seconds"] <= max_age_seconds


if __name__ == "__main__":
    import sys
    client = Boternity()
    name = sys.argv[1] if len(sys.argv) > 1 else "time"
    args = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
    print(json.dumps(client.call(name, args), indent=1, ensure_ascii=False))
