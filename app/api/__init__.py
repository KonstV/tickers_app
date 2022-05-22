from fastapi import APIRouter

from .ticker import router as ticker_router
from .status import router as status_router

router = APIRouter()
router.include_router(ticker_router)
router.include_router(status_router)
