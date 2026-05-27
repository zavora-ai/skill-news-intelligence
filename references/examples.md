# News Examples

## Example 1: "What's happening in Kenya today?"
```
get_country_news(country: "KE") → [{title: "Kenya GDP grows 5.1%...", source: "Reuters"}, ...]
get_trending_topics(country: "KE") → ["economy", "elections", "tech"]
```
Response: "Top Kenya news: GDP growth 5.1% (Reuters). Trending: economy, elections, tech."

## Example 2: "What's the media saying about AI agents?"
```
search_news(query: "AI agents enterprise", time_range: "7d") → 45 articles
get_news_sentiment(query: "AI agents") → {positive: 68%, neutral: 27%, negative: 5%}
```
Response: "45 articles in 7 days. Sentiment: overwhelmingly positive (68%). Key themes: productivity, automation."
