import datetime as dt
from sqlalchemy import Column, Integer, String, TIMESTAMP

from .database import Base

class Ticker(Base):
    __tablename__ = "tickers"

    ticker = Column(String, primary_key=True)
    datetime = Column(TIMESTAMP, default=dt.datetime.utcnow, primary_key=True)
    price = Column(Integer)
