#!/bin/sh
# Every BOTERNITY tool is also a plain REST call (no key needed). Same 9 tools as the MCP server.
curl -X POST https://boternity.com/api/public/v4/tools/get_data \
  -H "Content-Type: application/json" -d '{"feed": "exchange_rates", "params": {"base": "EUR", "symbols": ["USD", "JPY"]}}'
curl -X POST https://boternity.com/api/public/v4/tools/find_mcp_server \
  -H "Content-Type: application/json" -d '{"need": "postgres"}'
curl -X POST https://boternity.com/api/public/v4/tools/time \
  -H "Content-Type: application/json" -d '{"operation": "convert", "datetime": "2026-03-29T01:30:00Z", "timezone": "Europe/Paris"}'
