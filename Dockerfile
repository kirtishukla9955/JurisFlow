FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app_root

RUN apt-get update && apt-get install -y \
    curl \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml .
RUN pip install --no-cache-dir .

COPY . .
