from fastapi import APIRouter

from apis.v1 import route_user


_api_router = APIRouter()
_api_router.include_router(route_user.router,prefix="",tags=["users"])