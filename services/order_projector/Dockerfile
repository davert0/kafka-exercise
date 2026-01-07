FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml /app/pyproject.toml
COPY services /app/services
COPY pkg /app/pkg

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir .

ENV PYTHONUNBUFFERED=1

CMD ["sh", "-c", "uvicorn services.order_projector.app.main:app --host 0.0.0.0 --port ${PORT:-8002} --log-level $(echo \"${LOG_LEVEL:-info}\" | tr '[:upper:]' '[:lower:]')"]
