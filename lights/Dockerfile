FROM python:3.11-alpine

RUN apk update \
    && apk add --no-cache gcc

WORKDIR /app

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . /app

ENV PYTHONUNBUFFERED 1

CMD ["python", "main.py"]
