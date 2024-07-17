import requests

from app.core.settings import settings


async def fetch_trending_news(country: str = "us", category: str = "technology"):
    url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={settings.NEWS_API_KEY}"
    response = requests.get(url)
    return response.json()
