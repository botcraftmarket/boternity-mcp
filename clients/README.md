# Official clients

Two small clients, one file each, no dependency. Both call the public REST API (`https://boternity.com/api/public/v4`),
which runs exactly the same tools as the MCP server. No key needed.

## Python (3.8+, standard library only)

Copy [`python/boternity.py`](python/boternity.py) next to your code:

```python
from boternity import Boternity, is_fresh

bt = Boternity()
quakes = bt.get_data("earthquakes", min_magnitude=5, limit=3)
if is_fresh(quakes, max_age_seconds=3600):
    print(quakes["data"])
print(bt.find_mcp_server(need="postgres", limit=3)["results"][0]["url"])
report = bt.test_mcp_server("https://example.com/mcp")   # waits for the finished report
grade = bt.check_site_for_agents("https://example.com")["grade"]
```

Command line: `python boternity.py get_data '{"feed": "feeds_status"}'`.

## JavaScript (Node 18+, Deno, Bun, browsers)

Copy [`js/boternity.mjs`](js/boternity.mjs):

```js
import { Boternity, isFresh } from "./boternity.mjs";

const bt = new Boternity();
const rates = await bt.getData("exchange_rates", { base: "EUR", symbols: ["USD", "JPY"] });
console.log(rates.data, isFresh(rates, 86400));
const page = await bt.readPage("https://example.com");
```

## Both clients

- One method per tool (`read_page`, `check_site_for_agents`, `watch_page`, `test_mcp_server`, `find_mcp_server`,
  `get_data`, `notebook`, `process_data`, `time`), plus `call(name, args)`, `tools()` and raw `mcp(method, params)`.
- `check_site_for_agents` and `test_mcp_server` wait for the finished result (polling every 3 s).
- Errors raise `BoternityError` with `.status` and `.detail`.
- Optional access key: `Boternity(key="btk_...")` / `new Boternity({ key: "btk_..." })`.
- `trust()` and `is_fresh()` / `isFresh()` read the [trust block](../methodology/trust-block.md).

License: MIT.
