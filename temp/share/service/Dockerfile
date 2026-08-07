FROM repo.nstart.cloud/dockerhub/python:3.11-slim

WORKDIR /app

RUN useradd -m appuser && mkdir -p /app/data /app/results && chown -R appuser:appuser /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY algo/ ./algo/
COPY api/ ./api/

USER appuser

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
