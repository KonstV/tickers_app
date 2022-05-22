import datetime as dt
from pydantic import BaseModel


class TickerBase(BaseModel):
    ticker: str
    datetime: dt.datetime
    price: int


class TickerCreate(TickerBase):
    pass


class Ticker(TickerBase):
    class Config:
        orm_mode = True
