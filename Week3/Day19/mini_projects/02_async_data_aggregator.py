"""
MINI PROJECT 2: Async Data Aggregator
=====================================
Build an async service that aggregates data from multiple sources

Requirements:
1. Fetch data from multiple APIs concurrently
2. Implement timeout handling for each source
3. Aggregate results even if some sources fail
4. Add caching to reduce API calls
5. Implement rate limiting for external API calls

Simulated data sources:
- Weather API
- News API
- Stock API
- Social Media API
"""

print("=" * 60)
print("ASYNC DATA AGGREGATOR")
print("=" * 60)

import asyncio
from typing import Dict, Any, Optional
from datetime import datetime, timedelta

# TODO: Implement the data aggregator

# 1. Cache class for storing results
# ----------------------------------
# class SimpleCache:
#     def __init__(self, ttl_seconds: int = 300):
#         self.cache: Dict[str, tuple] = {}  # key -> (value, expiry_time)
#         self.ttl = ttl_seconds
#
#     def get(self, key: str) -> Optional[Any]:
#         pass
#
#     def set(self, key: str, value: Any):
#         pass


# 2. Individual data fetchers (simulate API calls)
# ------------------------------------------------
# async def fetch_weather(city: str, timeout: float = 5.0) -> dict:
#     """Fetch weather data for a city."""
#     await asyncio.sleep(0.5)  # Simulate API latency
#     return {
#         "source": "weather",
#         "city": city,
#         "temperature": 72,
#         "conditions": "sunny"
#     }
#
# async def fetch_news(topic: str, timeout: float = 5.0) -> dict:
#     """Fetch news for a topic."""
#     pass
#
# async def fetch_stocks(symbol: str, timeout: float = 5.0) -> dict:
#     """Fetch stock data for a symbol."""
#     pass
#
# async def fetch_social(hashtag: str, timeout: float = 5.0) -> dict:
#     """Fetch social media data for a hashtag."""
#     pass


# 3. Aggregator class
# -------------------
# class DataAggregator:
#     def __init__(self):
#         self.cache = SimpleCache(ttl_seconds=300)
#         self.semaphore = asyncio.Semaphore(5)  # Max 5 concurrent requests
#
#     async def fetch_with_timeout(self, coro, timeout: float) -> Optional[dict]:
#         """Fetch data with timeout, return None on failure."""
#         try:
#             async with self.semaphore:
#                 return await asyncio.wait_for(coro, timeout=timeout)
#         except asyncio.TimeoutError:
#             return None
#         except Exception as e:
#             return {"error": str(e)}
#
#     async def aggregate(self, params: dict) -> dict:
#         """Aggregate data from all sources."""
#         results = await asyncio.gather(
#             self.fetch_with_timeout(fetch_weather(params.get("city")), 5.0),
#             self.fetch_with_timeout(fetch_news(params.get("topic")), 5.0),
#             self.fetch_with_timeout(fetch_stocks(params.get("symbol")), 5.0),
#             self.fetch_with_timeout(fetch_social(params.get("hashtag")), 5.0),
#             return_exceptions=True
#         )
#         
#         return {
#             "weather": results[0],
#             "news": results[1],
#             "stocks": results[2],
#             "social": results[3],
#             "timestamp": datetime.now().isoformat()
#         }


# 4. FastAPI integration
# ----------------------
# from fastapi import FastAPI
# 
# app = FastAPI()
# aggregator = DataAggregator()
#
# @app.get("/aggregate")
# async def get_aggregated_data(
#     city: str = "New York",
#     topic: str = "technology",
#     symbol: str = "AAPL",
#     hashtag: str = "tech"
# ):
#     result = await aggregator.aggregate({
#         "city": city,
#         "topic": topic,
#         "symbol": symbol,
#         "hashtag": hashtag
#     })
#     return result


# BONUS: Add these features
# -------------------------
# - Persistent caching with Redis
# - Retry logic for failed requests
# - Health check endpoint
# - Metrics collection (response times, cache hits)


print("\nImplement your data aggregator above!")
