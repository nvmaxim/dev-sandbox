from algo.sar_water_pipeline import run_full_pipeline
from fastapi import BackgroundTasks, FastAPI
from pydantic import BaseModel

app = FastAPI(title="SAR Water Detection API (Test)", version="1.0.0")


class ProcessRequest(BaseModel):
    order_id: str = "test-order-001"
    image_id: str = "S1A_IW_GRDH_TEST"


@app.get("/healthz")
def health_check():
    return {"status": "ok"}


@app.get("/readyz")
def ready_check():
    return {"status": "ready"}


@app.post("/process")
async def process_image(request: ProcessRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(
        run_full_pipeline,
        input_safe=f"/app/data/{request.image_id}",
        graph_file="/app/pipeline.xml",
        output_dir=f"/app/results/{request.image_id}",
    )
    return {"status": "accepted", "message": f"Заказ {request.order_id} принят."}
