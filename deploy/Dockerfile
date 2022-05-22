FROM python:3.10-slim as base

ENV WORKDIR=/app

WORKDIR $WORKDIR

RUN apt-get update && apt-get install -y --no-install-recommends build-essential libpq-dev curl

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

FROM base

WORKDIR $WORKDIR

COPY ./app ./app
COPY ./migration ./migration
COPY ./alembic.ini ./alembic.ini
COPY startup.sh ./
RUN chmod +x ./startup.sh

CMD ["./startup.sh"]
