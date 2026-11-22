#!/bin/sh
# Every BOTERNITY tool is also a plain REST call (no key needed).
curl -X POST https://boternity.com/api/public/v4/tools/get_exchange_rates \
  -H "Content-Type: application/json" -d '{"base": "EUR", "symbols": ["USD", "JPY"]}'
curl -X POST https://boternity.com/api/public/v4/tools/find_mcp_server \
  -H "Content-Type: application/json" -d '{"need": "postgres"}'
