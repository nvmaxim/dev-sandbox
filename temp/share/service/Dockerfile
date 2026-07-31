FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    wget curl bash default-jre libgomp1 \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash appuser

WORKDIR /app
RUN mkdir -p /app/results /app/data && chown -R appuser:appuser /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY algo/ ./algo/
COPY api/ ./api/

USER appuser

EXPOSE 8000
ENTRYPOINT ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
