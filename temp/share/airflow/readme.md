# Airflow DAGs Repository (`tsuod-geoservices`)

Репозиторий для хранения и автоматической доставки сценариев (DAGs) планировщика Apache Airflow.

## Структура
* `dags/` — файлы сценариев Airflow. Группируйте их по подпапкам (например, `dags/infrastructure/`, `dags/integrations/`).
* `utils/` — общие модули, хелперы и функции уведомлений.
* `tests/` — автоматические тесты проверки синтаксиса.

## Правила разработки
1. Создаем ветку: `git checkout -b feature/new-dag-name`
2. Кладем DAG в папку `dags/`
3. Проверяем синтаксис локально: `pytest tests/`
4. Делаем push и создаем Merge Request в ветку `main`.
