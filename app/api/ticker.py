from fastapi import APIRouter
from fastapi import Depends, Query, Path
from sqlalchemy.orm import Session

from typing import List

from ..database import get_db
from ..models import Ticker
from ..operations import get_tickers, get_ticker_data

router = APIRouter(
    prefix='/api'
)

@router.get('/tickers')
def get_tickers_ep(db: Session = Depends(get_db)):
    return [t["ticker"] for t in get_tickers(db)]

@router.get('/ticker/{ticker_id}')
def get_ticker_data_ep(
        db: Session = Depends(get_db),
        ticker_id: str = Path(),
        limit: int = Query(default=10)):
    return get_ticker_data(db, ticker_id, limit=limit)
