FROM python:3.11-slim

# RUN apk update \
#     && apk add --no-cache gcc
RUN apt update \
    && apt install -y gcc \
    && rm -rf /vat/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . /app

ENV PYTHONUNBUFFERED 1

CMD ["python", "main.py"]
