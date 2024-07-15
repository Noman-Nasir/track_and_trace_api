"""
Weather info utility
"""
import datetime as dt
from typing import Dict, List

import aiohttp
import pytz
from fastapi import HTTPException

from config import get_meteomatics_credentials


class RESTError(HTTPException):
    """
    Custom HTTPException used to differentiate errors thrown when using the
    call_rest function
    """


async def get_weather_info(session: aiohttp.ClientSession, country_code: str, zipcode: str) -> List[Dict[str, str]]:
    """
    Fetches weather info from meteomatics weather api

    Args:
        session: http session to make calls
        country_code: ISO 3166-1 alpha-2 format country code
        zipcode: Numeric zip code
    Returns:
        Weather info List e.g., [{"t_2m:C": 32.1},{"wind_speed_10m:ms": 6.2}]
        t_2m:C is Instantaneous temperature at 2m above ground in degrees Celsius
        wind_speed_10m:ms is Instantaneous wind speed at 10m above ground
    Raises:
        RESTError in case of network failure or invalid/bad request
    """
    postal = f"postal_{country_code}{zipcode}"
    # Format date to required from by meteomatics api
    date = dt.datetime.now().replace(tzinfo=pytz.UTC).isoformat()
    # Get creds from env file
    username, password = get_meteomatics_credentials()
    try:
        response = await session.get(
            url=f"https://api.meteomatics.com/{date}/t_2m:C,wind_speed_10m:ms/{postal}/json",
            auth=aiohttp.BasicAuth(username, password)
        )
    except aiohttp.ClientConnectorError as exc:
        raise RESTError(
            status_code=500, detail="Could not make the call"
        ) from exc

    if response.ok:
        weather_info = await response.json()
        # format the weather data such that List[Dict["parameter_name", "parameter_value"]]
        parsed_weather = [{w["parameter"]: w["coordinates"][0]["dates"][0]["value"]} for w in weather_info["data"]]
        return parsed_weather

    try:
        error = await response.json()
        errors = [{"reason": "Invalid address", "msg": error["message"]}]
    except (aiohttp.ContentTypeError, KeyError):
        errors = [{"msg": response.reason}]

    raise RESTError(status_code=response.status, detail=errors)
