"""
Api routes
"""
from fastapi import APIRouter

from api.endpoints import track

api_router = APIRouter()

API_ROUTES = [
    ("/track/{tracking_number}", track.router, ["track"]),
]

for prefix, router, tags in API_ROUTES:
    api_router.include_router(router=router, prefix=prefix, tags=tags)
