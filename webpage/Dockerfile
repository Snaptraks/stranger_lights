FROM python:3.12-alpine AS builder

WORKDIR /app

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . /app

ENV PYTHONUNBUFFERED 1

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
