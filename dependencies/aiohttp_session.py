"""
Helper functions related to use of aiohttp with fastapi
"""
import aiohttp


async def aiohttp_session():
    """
    Used in conjunction with the aiohttp requests in an async function,
    required to communicate with the weather api
    """
    async with aiohttp.ClientSession() as session:
        yield session
