# Stage 1: Builder
FROM python:3.9-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt uvicorn

# Stage 2: Runtime
FROM python:3.9-slim

WORKDIR /app

RUN useradd --create-home appuser && chown -R appuser:appuser /app
USER appuser

COPY --from=builder /usr/local /usr/local
COPY . /app

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--workers", "4"]
