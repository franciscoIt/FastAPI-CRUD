from fastapi import APIRouter

from apis.v1 import route_user,route_blog


_api_router = APIRouter()
_api_router.include_router(route_user.router,prefix="",tags=["users"])
_api_router.include_router(route_blog.router,prefix="",tags=["blogs"])