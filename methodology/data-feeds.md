# Open data feeds (get_data)

Live: <https://boternity.com/data> · freshness of every feed: <https://boternity.com/data/status.json>

**How.** A deterministic collector (no AI model) fetches each official source over HTTPS on a fixed schedule, parses it
and checks it before replacing the previous copy. If a fetch fails, the last good copy is kept and marked **stale** (older
than 3 refresh intervals plus 10 minutes). Values are passed on unchanged, with the source's license and attribution.

Every answer carries `source`, `source_url`, `license`, `attribution`, `updated_at` (time given by the source),
`fetched_at` (time of our fetch), `stale`, and a [trust block](trust-block.md).

The list of feeds, their sources and refresh rates is generated from the server code in the main
[README](../README.md#get_data-feeds).

**Limits.** BOTERNITY checks that values come unchanged from the source, not that the source is right. Each feed's own
limits (forecasts are model output, reference exchange rates are not transaction rates, preprints are not peer-reviewed…)
are listed in the `limitations` field of its trust block.
