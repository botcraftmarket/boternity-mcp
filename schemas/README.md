# Schemas

Generated from the server code (never edited by hand):

- [`tools.json`](tools.json): the listed tools exactly as MCP `tools/list` returns them (name, description, input schema,
  output schema, annotations), with the server version.
- [`trust.schema.json`](trust.schema.json): JSON Schema (2020-12) of the `trust` block found in answers that state facts
  or scores. See [methodology/trust-block.md](../methodology/trust-block.md).

Compatibility: tool names and arguments are only ever added; a tool that is merged or renamed keeps answering under its
older name. Within `boternity.trust/1`, trust fields are only added, never renamed or removed.
