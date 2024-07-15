"""
Track endpoints.
"""

import cachetools
import sqlalchemy
from fastapi import APIRouter, Depends, HTTPException

from api.schemas.track import TrackOrderResponse
from db import crud
from dependencies import aiohttp_session, cache, db
from utils.common import parse_address, is_valid_address
from utils.weather import get_weather_info

router = APIRouter()


@router.get(
    "",
    name="Get order status and weather report",
    response_model=TrackOrderResponse,
)
async def track_order(
        tracking_number: str,
        http_session=Depends(aiohttp_session.aiohttp_session),
        cache_instance: 'cachetools.TTLCache' = Depends(cache.get_weather_cache),
        db_session: 'sqlalchemy.orm.session.Session' = Depends(db.db_session)
):
    """
    Retrieve Order status and weather info at receiver's address

    Args:
        tracking_number: tracking_number
        http_session: aiohttp session
        cache_instance: Cache instance
        db_session: database instance

    Raises:
        HTTPException: if order with the given tracking number is not found
    """

    # Retrieve order with the associated tracking_number
    order = crud.get_order(db_session, tracking_number)

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    # Create a list of article dicts to have richer response object
    articles = []
    for order_article in order.order_articles:
        article = dict(order_article.article.__dict__)
        # Remove _sa_instance_state key as it is not needed
        article.pop('_sa_instance_state')
        article["quantity"] = order_article.article_quantity
        articles.append(article)

    # This should be checked when creating the order. Adding here just to avoid unnecessary errors
    address = order.receiver_address
    if not is_valid_address(address):
        # We should still return the order status and articles
        return {
            "weather": "Invalid address. Unable to retrieve weather data.",
            "articles": articles,
            "status": order.status,
        }

    try:
        zipcode, country_code = parse_address(order.receiver_address)
    except KeyError:
        # Raised incase country name cannot be mapped to a country code
        return {
            "weather": "Invalid address. Unable to retrieve weather data.",
            "articles": articles,
            "status": order.status,
        }

    # Check if weather info for the zipcode and country_code combo exists
    weather = cache_instance.get((zipcode, country_code))
    if not weather:
        weather = await get_weather_info(http_session, country_code=country_code, zipcode=zipcode)
        cache_instance.update({(zipcode, country_code): weather})

    return {
        "weather": weather,
        "articles": articles,
        "status": order.status,
    }
