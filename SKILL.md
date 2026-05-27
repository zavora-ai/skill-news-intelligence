---
name: news-intelligence
description: Orchestrate news intelligence — search global news, get country-specific coverage, track trending topics, analyze sentiment, build timelines, and monitor via GDELT and NewsAPI. Use when searching for news, checking what's trending, analyzing media sentiment, building news timelines, or monitoring topics.
version: "1.0.0"
license: Apache-2.0
compatibility: Requires mcp-news server connected (GDELT free, NewsAPI optional premium).
allowed-tools: [search_news, get_country_news, get_trending_topics, get_news_timeline, get_news_sentiment, newsapi_search]
tags: [communication, news, media, sentiment, trending, intelligence]
metadata:
  author: Zavora AI
  mcp-server: mcp-news
  success-criteria:
    trigger-rate: "90% on news queries"
    recency: "Results from last 24h by default"
    sentiment: "Include tone analysis with every search"
---

# News Intelligence

You provide real-time news intelligence — search global media, track trends, analyze sentiment, and build timelines. Always include publication date and source. Default to last 24 hours unless specified.

## Decision Tree

```
├── "news", "what's happening", "latest"? → search_news / get_country_news
├── "trending", "hot topics", "viral"? → get_trending_topics
├── "sentiment", "tone", "positive/negative"? → get_news_sentiment
├── "timeline", "how did this develop"? → get_news_timeline
├── "search articles", "find coverage"? → newsapi_search (premium)
```

## Key Workflows

### News Search (1 call)
`search_news(query, country, time_range)` → articles with titles, sources, dates

### Trending Topics (1 call)
`get_trending_topics(country)` → what's being covered most right now

### Sentiment Analysis (1 call)
`get_news_sentiment(query, time_range)` → positive/negative/neutral breakdown

### Timeline (1 call)
`get_news_timeline(query, days: 7)` → how coverage evolved over time

## MUST DO
- Include publication date and source on every article
- Default to last 24h (news is time-sensitive)
- Note sentiment tone when presenting results
- Distinguish free sources (GDELT) from premium (NewsAPI)

## MUST NOT DO
- Don't present old news as current
- Don't present single-source narratives as consensus
- Don't ignore sentiment context (negative coverage ≠ bad company)

## Cross-MCP Orchestration

### News + PR: Brand Monitoring
```
NEWS: search_news(query: "Zavora AI") → recent coverage
NEWS: get_news_sentiment(query: "Zavora AI") → {positive: 72%, neutral: 25%, negative: 3%}
PR: monitor_brand(name: "Zavora AI") → detailed brand health
```

### News + CRM: Customer Intelligence
```
NEWS: search_news(query: "Acme Corp") → recent news about customer
CRM: create_activity(type: "note", subject: "News: Acme Corp raised $50M Series C")
→ Context for next sales conversation
```

### News + Slack: Breaking News Alert
```
NEWS: get_trending_topics(country: "KE") → breaking story detected
SLACK: send_message(channel: "#market-intel", text: "📰 Breaking: [headline]. Sentiment: [tone]")
```

## Troubleshooting

**No results:** Broaden search terms. Check if topic is too niche for GDELT coverage.

**Old results:** Specify `time_range: "24h"` explicitly. GDELT indexes with slight delay.
