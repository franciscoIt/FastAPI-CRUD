from apis.v1 import route_blog
from apis.v1 import route_user
from fastapi import APIRouter


_api_router = APIRouter()
_api_router.include_router(route_user.router, prefix="", tags=["users"])
_api_router.include_router(route_blog.router, prefix="", tags=["blogs"])
