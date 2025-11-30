"""
MINI PROJECT 2: Build and Test a Weather Service
=================================================
Build a weather service that fetches data from an external API,
then write comprehensive tests with mocking

Requirements:
1. Implement the WeatherService class
2. Write unit tests with mocking
3. Handle all error cases
4. Use fixtures and parametrized tests
5. Test caching functionality
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum


# ========== MODELS ==========

class WeatherCondition(Enum):
    SUNNY = "sunny"
    CLOUDY = "cloudy"
    RAINY = "rainy"
    SNOWY = "snowy"
    STORMY = "stormy"


@dataclass
class WeatherData:
    """Weather data model."""
    city: str
    country: str
    temperature: float  # Celsius
    humidity: int  # Percentage
    condition: WeatherCondition
    wind_speed: float  # km/h
    timestamp: datetime


@dataclass
class ForecastDay:
    """Single day forecast."""
    date: datetime
    high_temp: float
    low_temp: float
    condition: WeatherCondition
    precipitation_chance: int


# ========== EXCEPTIONS ==========

class WeatherServiceError(Exception):
    """Base exception for weather service."""
    pass


class CityNotFoundError(WeatherServiceError):
    """City not found."""
    def __init__(self, city: str):
        super().__init__(f"City '{city}' not found")
        self.city = city


class APIError(WeatherServiceError):
    """External API error."""
    def __init__(self, status_code: int, message: str):
        super().__init__(f"API error ({status_code}): {message}")
        self.status_code = status_code


class RateLimitError(WeatherServiceError):
    """Rate limit exceeded."""
    def __init__(self, retry_after: int):
        super().__init__(f"Rate limit exceeded. Retry after {retry_after} seconds")
        self.retry_after = retry_after


# ========== CACHE ==========

class WeatherCache:
    """Simple in-memory cache for weather data."""
    
    def __init__(self, ttl_seconds: int = 300):
        self._cache: Dict[str, tuple] = {}  # key -> (data, expiry_time)
        self._ttl = ttl_seconds
    
    def get(self, key: str) -> Optional[any]:
        """Get cached value if not expired."""
        if key in self._cache:
            data, expiry = self._cache[key]
            if datetime.now() < expiry:
                return data
            else:
                del self._cache[key]
        return None
    
    def set(self, key: str, value: any):
        """Cache a value."""
        expiry = datetime.now() + timedelta(seconds=self._ttl)
        self._cache[key] = (value, expiry)
    
    def clear(self):
        """Clear all cached data."""
        self._cache.clear()
    
    def invalidate(self, key: str):
        """Invalidate specific cache entry."""
        if key in self._cache:
            del self._cache[key]


# ========== YOUR TASK: IMPLEMENT WEATHER SERVICE ==========

class WeatherService:
    """
    Weather service that fetches data from external API.
    
    TODO: Implement the following methods:
    1. get_current_weather(city) - Get current weather for a city
    2. get_forecast(city, days) - Get weather forecast
    3. get_multiple_cities(cities) - Get weather for multiple cities
    4. Use caching to avoid unnecessary API calls
    5. Handle all error cases properly
    """
    
    def __init__(self, api_key: str, cache: WeatherCache = None):
        self.api_key = api_key
        self.base_url = "https://api.weather.example.com"
        self._cache = cache or WeatherCache()
    
    def get_current_weather(self, city: str) -> WeatherData:
        """
        Get current weather for a city.
        
        TODO: Implement this method:
        1. Check cache first
        2. Make API request if not cached
        3. Parse response into WeatherData
        4. Handle errors (404 -> CityNotFoundError, 429 -> RateLimitError, etc.)
        5. Cache the result
        
        Expected API response format:
        {
            "city": "London",
            "country": "UK",
            "temperature": 15.5,
            "humidity": 80,
            "condition": "cloudy",
            "wind_speed": 20.5
        }
        """
        # TODO: Implement
        pass
    
    def get_forecast(self, city: str, days: int = 5) -> List[ForecastDay]:
        """
        Get weather forecast for a city.
        
        TODO: Implement this method:
        1. Validate days (1-10)
        2. Check cache
        3. Make API request
        4. Parse response into list of ForecastDay
        5. Handle errors
        6. Cache result
        
        Expected API response format:
        {
            "city": "London",
            "forecast": [
                {
                    "date": "2024-01-15",
                    "high": 12.0,
                    "low": 5.0,
                    "condition": "rainy",
                    "precipitation_chance": 80
                },
                ...
            ]
        }
        """
        # TODO: Implement
        pass
    
    def get_multiple_cities(self, cities: List[str]) -> Dict[str, WeatherData]:
        """
        Get weather for multiple cities.
        
        TODO: Implement this method:
        1. Fetch weather for each city
        2. Return dict mapping city name to WeatherData
        3. Handle individual city errors gracefully
        4. Return partial results if some cities fail
        """
        # TODO: Implement
        pass
    
    def _make_api_request(self, endpoint: str, params: Dict = None) -> Dict:
        """
        Make API request.
        
        TODO: Implement this helper method:
        1. Build request URL
        2. Add API key to headers
        3. Make request
        4. Handle response codes
        5. Return parsed JSON
        """
        # TODO: Implement
        pass
    
    def _parse_weather_data(self, data: Dict) -> WeatherData:
        """Parse API response into WeatherData."""
        # TODO: Implement
        pass
    
    def _parse_forecast(self, data: Dict) -> List[ForecastDay]:
        """Parse API response into list of ForecastDay."""
        # TODO: Implement
        pass


# ========== YOUR TASK: WRITE TESTS ==========

"""
TODO: Write comprehensive tests for WeatherService:

1. TestWeatherCache
   - test_cache_set_and_get
   - test_cache_expiry
   - test_cache_clear
   - test_cache_invalidate

2. TestGetCurrentWeather
   - test_get_weather_success
   - test_get_weather_from_cache
   - test_get_weather_city_not_found
   - test_get_weather_api_error
   - test_get_weather_rate_limit

3. TestGetForecast
   - test_get_forecast_success
   - test_get_forecast_invalid_days
   - test_get_forecast_city_not_found

4. TestGetMultipleCities
   - test_get_multiple_cities_all_success
   - test_get_multiple_cities_partial_failure
   - test_get_multiple_cities_empty_list

5. TestIntegration
   - test_caching_prevents_duplicate_requests
   - test_cache_invalidation_forces_new_request

Write your tests below:
"""

# Example fixtures
@pytest.fixture
def cache():
    """Provide a fresh cache."""
    return WeatherCache(ttl_seconds=300)


@pytest.fixture
def weather_service(cache):
    """Provide a weather service with mocked requests."""
    return WeatherService(api_key="test-key", cache=cache)


@pytest.fixture
def sample_weather_response():
    """Sample API response for current weather."""
    return {
        "city": "London",
        "country": "UK",
        "temperature": 15.5,
        "humidity": 80,
        "condition": "cloudy",
        "wind_speed": 20.5
    }


@pytest.fixture
def sample_forecast_response():
    """Sample API response for forecast."""
    return {
        "city": "London",
        "forecast": [
            {
                "date": "2024-01-15",
                "high": 12.0,
                "low": 5.0,
                "condition": "rainy",
                "precipitation_chance": 80
            },
            {
                "date": "2024-01-16",
                "high": 14.0,
                "low": 7.0,
                "condition": "cloudy",
                "precipitation_chance": 40
            }
        ]
    }


# Start writing your tests here:


"""
Run your tests with: pytest 02_weather_service_tests.py -v --cov=. --cov-report=term-missing
"""
