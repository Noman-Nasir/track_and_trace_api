"""
Helper functions related to caching in fastapi
"""

import cachetools

from constants import WEATHER_CACHE_TTL

weather_cache = cachetools.TTLCache(128, WEATHER_CACHE_TTL)


def get_weather_cache():
    """
    Returns weather cache instance
    """
    return weather_cache
