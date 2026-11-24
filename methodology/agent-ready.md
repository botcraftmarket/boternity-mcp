# Agent-ready score (scoring v2, since 23 November 2026)

Canonical page: <https://boternity.com/agent-check/method>

BOTERNITY sends one honest, declared AI agent (`BOTERNITY-AgentCheck/1.0`) to the home page of a site, **without running
JavaScript**, with at most 6 requests and `robots.txt` respected, and counts the points the site earns on three questions.
100 means perfect on every criterion. (Before v2, the score started at 100 and only lost points on problems.)

## Can an AI agent get in? 30 points

| Criterion | Points | How to earn them |
| --- | --- | --- |
| Page opens for a declared bot | gate | A bot wall, a 403/429 refusal or no answer gives grade **F**, whatever the rest. |
| Speed | 8 | 8 under 300 ms, 6 under 800 ms, 3 under 2 s. If the page takes 300 ms or more and the site already announces its MCP server in llms.txt, the page is timed a second time and the better time counts. This second timing never costs a site anything. |
| HTTPS | 6 | The page is served over HTTPS. |
| robots.txt | 4 | Present and readable (2 if absent). |
| AI search and assistant bots allowed | 12 | Share of ChatGPT-User, OAI-SearchBot, Claude-User, Claude-SearchBot, PerplexityBot, Perplexity-User, Googlebot, Bingbot… allowed. Blocking training bots (GPTBot, ClaudeBot, CCBot…) is the site's choice and costs nothing. |

## Can it understand the page? 35 points

| Criterion | Points | How to earn them |
| --- | --- | --- |
| Text readable without JavaScript | 8 | 8 from 300 words in the HTML, 6 from 150, 3 from 40. |
| Title and description | 5 | Title of 10–70 characters (2), description of 50–170 characters (3). |
| Language | 2 | `<html lang>`. |
| Canonical address | 2 | `<link rel="canonical">`. |
| Headings | 3 | Exactly one `<h1>` (2) and `<h2>` sections (1). |
| Images described | 2 | At least 90 % of images have an `alt` attribute (1 from 50 %). |
| Structured data (schema.org) | 7 | Valid JSON-LD (2), Organization or WebSite (1), types of what you offer such as Product/Offer, LocalBusiness, Article, Event (up to 2), BreadcrumbList or FAQPage (1), no invalid block (1). |
| XML sitemap | 3 | Readable by a declared bot. |
| llms.txt | 3 | A plain-text guide for language models (llmstxt.org). |

## Can it take action? 35 points

| Criterion | Points | How to earn them |
| --- | --- | --- |
| Forms | 4 | Every field labelled (2 when the page has no form). |
| Contact | 4 | A contact page, e-mail or phone easy to find. |
| Search | 3 | schema.org SearchAction (1 for a plain search field). |
| API description | 8 | An OpenAPI description announced (`rel="service-desc"`, api-catalog, Link header or llms.txt); 3 for a developer link only. |
| MCP server | 8 | Announced in llms.txt or `/.well-known/mcp.json`. |
| A2A agent card | 4 | `/.well-known/agent-card.json`. |
| Offers as data | 4 | schema.org Offer with price and availability (2 with price only). |

**Grades:** A ≥ 90 · B ≥ 75 · C ≥ 60 · D ≥ 40 · E below 40 · F when an agent cannot get in.

## Limits

One home page, one pass, from one server in Europe, without JavaScript: the result is what most AI agents and crawlers
see, not what a full browser sees. A site can answer differently at another time or to another address. The test is
automatic and can be wrong; walls against bots are often a deliberate choice.

Run it: <https://boternity.com/agent-check> · MCP tool `check_site_for_agents`.
