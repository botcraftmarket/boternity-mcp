# Trust block (`boternity.trust/1`)

Page: <https://boternity.com/trust> · JSON Schema: [`schemas/trust.schema.json`](../schemas/trust.schema.json)

Answers that state a fact or a score contain a `trust` object **in their content** (tool schemas are unchanged, so
existing clients are not affected): `get_data`, `find_mcp_server`, `check_site_for_agents`, `test_mcp_server` (finished
report) and `read_page`, plus the open files `/mcp-index/data.json` and `/mcp-weather.json`.

| Field | Meaning |
| --- | --- |
| `schema_version` | `boternity.trust/1`. Within one version, fields are only added, never renamed or removed. |
| `source`, `source_url` | The original publisher, or BOTERNITY for its own measurements. |
| `observed_at` | When the data was collected or measured (ISO 8601 UTC). |
| `verified_at` | When BOTERNITY last checked it; `null` when nothing was checked beyond fetching (`read_page`). |
| `verification_method` | What was checked, in one sentence. |
| `freshness_seconds` | Age of `observed_at` when the answer was sent. |
| `data_status` | `fresh`, `stale` (last fetch failed, older copy kept), `live` (checked every few minutes), `nightly` (checked once a night), `pending` (measurement running) or `unavailable`. |
| `limitations` | What the data does not tell you. Read it before acting. |
| `method_url`, `report_error_url` | <https://boternity.com/trust> and its error report form. |

Tip for agents: act on an answer only when `data_status` is not `stale`, `pending` or `unavailable` and
`freshness_seconds` fits your need. Both official clients have an `is_fresh` / `isFresh` helper.

Real examples: [`examples/responses/`](../examples/responses/).
