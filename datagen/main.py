import datetime as dt
from random import random
import time

from app.database import get_db
from app.models import Ticker
from app.operations import insert_tickers_data

import numpy as np

INTERVAL = 1.0
TICKERS_CNT = 10

prices = np.array([0] * TICKERS_CNT)

def generate_movement() -> int:
    movement = -1 if random() < 0.5 else 1
    return movement


def generate_data() -> None:
    print("Datagen process started")
    global prices
    while True:
        start_time = dt.datetime.now()
        datetime = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tickers = [Ticker(ticker=f"ticker_{i:0>2}", datetime=datetime, price=int(prices[i])) for i in range(TICKERS_CNT)]
        session = next(get_db())
        insert_tickers_data(session, tickers)
        prices += np.array([generate_movement() for _ in range(TICKERS_CNT)])
        cur_time = dt.datetime.now()
        sleep_time = INTERVAL * 10**6 - ((cur_time - start_time) / dt.timedelta(microseconds=1)) # оставшееся время сна в микросекундах
        if sleep_time > 0:
            time.sleep(sleep_time / 10**6)


def main() -> None:
    generate_data()


if __name__ == '__main__':
    main()
