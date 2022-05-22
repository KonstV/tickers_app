#!/usr/bin/env sh

alembic upgrade head
python3 -m app.main
