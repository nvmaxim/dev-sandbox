from fastapi import BackgroundTasks, FastAPI
from fastapi.responses import Response
from prometheus_client import CONTENT_TYPE_LATEST, Counter, generate_latest
from pydantic import BaseModel

app = FastAPI(
    title="Geoservice Template API",
    description="Шаблон",
    version="1.0.0",
)

TASKS_PROCESSED = Counter("tasks_processed_total", "Total processed tasks", ["status"])


class ProcessRequest(BaseModel):
    order_id: str
    image_id: str


@app.get("/healthz")
def health_check():
    return {"status": "ok"}


@app.get("/readyz")
def ready_check():
    return {"status": "ready"}


@app.get("/metrics")
def get_metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


def background_processing(order_id: str, image_id: str):
    print(f"[{image_id}] Запуск фоновой задачи для заказа {order_id}...")


@app.post("/process")
async def process_task(request: ProcessRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(background_processing, request.order_id, request.image_id)
    return {
        "status": "accepted",
        "message": f"Заказ {request.order_id} принят в работу.",
    }
