import logging
import time

from fastapi import BackgroundTasks, FastAPI
from pydantic import BaseModel

# --- Настройка логирования ---
logging.basicConfig(level=logging.INFO)

# --- Инициализация FastAPI ---
app = FastAPI(
    title="Geo Processing Service",
    description="Сервис асинхронной обработки географических снимков",
)


# --- 1. Модель входящих данных (JSON-контракт) ---
class OrderPayload(BaseModel):
    order_id: str
    input_image_path: str


# --- 2. Вспомогательная функция обновления статуса ---
def update_order_status(order_id: str, status: str, error_message: str = None):
    """Эмуляция PATCH/PUT-запроса к сервису архива/БД для обновления статуса заказа."""
    payload = {"status": status}
    if error_message:
        payload["error"] = error_message
    logging.info(f"[API UPDATE] Заказ {order_id} -> Статус: {status}")


# --- 3. Фоновая задача (Worker Task) ---
def process_geo_data_task(order_id: str, input_image_path: str):
    """Фоновая логика: меняет статус на processing, выполняет имитацию долгих вычислений
    и при успехе переводит в delivered, а при ошибке — в failed.
    """
    try:
        # 1. Перевод в статус processing
        update_order_status(order_id, "processing")
        logging.info(f"Начало обработки файла: {input_image_path}")

        # Эмуляция долгой геообработки (GDAL / SNAP)
        time.sleep(2)

        # Проверка формата исходного файла
        if not input_image_path.endswith((".tif", ".SAFE")):
            raise ValueError("Неподдерживаемый формат исходного снимка")

        # 2. Успешное завершение -> перевод в status delivered
        logging.info("Генерация маски завершена. Файлы записаны в /app/results")
        update_order_status(order_id, "delivered")

    except Exception as e:
        # 3. Перехват ошибки -> перевод в status failed
        logging.error(f"Ошибка при обработке заказа {order_id}: {e!s}")
        update_order_status(order_id, "failed", error_message=str(e))


# --- 4. FastAPI Эндпоинт ---
@app.post("/api/process-order", status_code=202)
async def create_order(payload: OrderPayload, background_tasks: BackgroundTasks):
    """Принимает JSON с задачей, передает её в фоновый режим
    и мгновенно возвращает ответ 202 Accepted.
    """
    background_tasks.add_task(
        process_geo_data_task,
        order_id=payload.order_id,
        input_image_path=payload.input_image_path,
    )

    return {
        "status": "accepted",
        "order_id": payload.order_id,
        "message": "Запрос принят и отправлен на фоновую обработку",
    }


# --- Запуск сервера прямо из файла ---
if __name__ == "__main__":
    import uvicorn

    # Передаем сам объект app напрямую
    uvicorn.run(app, host="127.0.0.1", port=8000)
