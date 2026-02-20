# Stage 1: Build Stage
FROM python:3.12-slim as builder
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev python3-dev build-essential libjpeg-dev zlib1g-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

# Stage 2: Production Stage
FROM python:3.12-slim
WORKDIR /app

RUN addgroup --system app && adduser --system --group app && mkdir -p /app/db /app/staticfiles /app/media

RUN apt-get update && apt-get install -y --no-install-recommends netcat-openbsd libjpeg62-turbo libpq5 zlib1g libpng16-16 && rm -rf /var/lib/apt/lists/*

COPY --from=builder /app/wheels /wheels
RUN pip install --no-cache-dir /wheels/*

COPY --chown=app:app . .
RUN chown -R app:app /app/staticfiles /app/media /app/db && chmod +x /app/entrypoint.sh

USER app
ENTRYPOINT ["/app/entrypoint.sh"]

# Gunicorn command
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "1", "nemt.wsgi:application"]

