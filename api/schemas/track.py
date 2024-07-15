"""
Track endpoints.
"""
from typing import List, Dict

from pydantic import BaseModel

from db.schemas import Article


class TrackOrderArticle(Article):
    """
    TrackOrderArticle inherits Article and adds quantity property
    """
    quantity: int


class TrackOrderResponse(BaseModel):
    """
    TrackOrderResponse schema
    """
    articles: List[TrackOrderArticle]
    weather: List[Dict[str, float]] | str
    status: str
