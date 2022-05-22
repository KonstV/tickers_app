FROM python:3.10-slim as base

ENV WORKDIR=/datagen

WORKDIR $WORKDIR

RUN apt-get update && apt-get install -y --no-install-recommends build-essential libpq-dev curl

RUN pip3 install psycopg2-binary

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

FROM base

WORKDIR $WORKDIR

COPY ./app ./app
COPY ./datagen ./datagen

CMD ["python3", "-m", "datagen.main"]
