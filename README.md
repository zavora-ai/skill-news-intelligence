# News Intelligence Skill

> Real-time news intelligence for AI agents — global search, trending topics, sentiment analysis, and timelines via GDELT (free) and NewsAPI.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--news-green)](https://github.com/zavora-ai/mcp-news)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

| Workflow | Calls | What It Achieves |
|----------|-------|------------------|
| News Search | 1 | Articles by query/country |
| Trending | 1 | What's hot right now |
| Sentiment | 1 | Positive/negative/neutral tone |
| Timeline | 1 | How story evolved over days |

## Installation

```bash
git clone https://github.com/zavora-ai/skill-news-intelligence.git ~/.skills/skills/news-intelligence
```

## Requirements

**Required:** `mcp-news` (6 tools — GDELT free, NewsAPI optional)
**Cross-MCP:** `mcp-pr` (brand monitoring), `mcp-crm` (customer context)

## Success Criteria

| Metric | Target |
|--------|--------|
| Recency | Last 24h by default |
| Sentiment | Included with every search |
| Sources | Always cite publication + date |

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;" alt=""/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0 — Part of [ADK-Rust Enterprise](https://enterprise.adk-rust.com). Built with ❤️ by [Zavora AI](https://zavora.ai)
