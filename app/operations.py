import datetime as dt
from typing import List
from sqlalchemy.orm import Session

from . import models, schemas

def get_tickers(db: Session):
    #return db.query(models.Ticker).all()
    return db.query(models.Ticker).with_entities(models.Ticker.ticker).distinct(models.Ticker.ticker).all()


def get_tickers_data(db: Session, ticker_id: str, limit: int) -> list[schemas.Ticker]:
    return db.query(models.Ticker).filter(models.Ticker.ticker == ticker_id).limit(limit).all()


def insert_tickers_data(db: Session, tickers: list[models.Ticker]):
    db.bulk_save_objects(tickers)
    db.commit()
    # for t in tickers:
    #     db_ticker = models.Ticker(**t.dict())
    #     db.add(db_ticker)
    #     db.commit()
    #     db.refresh(db_ticker)
    return "Success"
