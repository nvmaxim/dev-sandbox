### Geoservice Microservice Template
Шаблон для создания и развертывания микросервисов геообработки в группе geoservices 

#### Структура проекта
```
├── algo/                     # сам алгоритм, xml, data/result, requirements_algo и тд 
├── api/                      # fastapi, эндпоинты
├── deploy/                   # k8s манифесты
├── docs/                     # документация
├── Dockerfile                # сборка докер образа
└── readme.md                 # описание сервиса
```
#### Разработчикам
Разработка алгоритмов геообработки ведется внутри директории algo/. Файлы за пределами этой папки (api/, deploy/, Dockerfile) редактировать не требуется
1. все нужные пакеты (numpy, rasterio и др) лучше добавить в файл algo/requirements_algo.txt
2. без хардкода. пути передаем через аргументы функции (входные файлы из /app/data/input, результат сохраняем в /app/data/output. оборачиваем в try/except для понимания ошибок
```python
# пример
def run_processing(input_path: str, output_path: str) -> dict:
    try:
        return {"status": "ok", "error": None}
    except Exception as e:
        return {"status": "error", "error": str(e)}
```
3. Для локального тестирования параметров и гиперпараметров без запуска веб-сервера добавляйте в конец вашего скрипта блок локального запуска:

```Python
if __name__ == "__main__":
    run_processing(
        input_path="./test_data/input.tif",
        output_path="./test_data/output.tif",
        params={"threshold": 0.5}
    )
```
#### Процесс разработки
Копируем репозиторий
```bash
git clone git@gitlab.your-domain.com:geoservices/your-service-name.git
```
Создаем ветку
```bash
git checkout -b feature/algo-implementation
```
Вносим изменения в папку algo/ и коммитим код
```bash
git add algo/
git commit -m "feat: добавлена маска бинаризации водных объектов"
```
Пушим ветку на сервер
```bash
git push origin feature/algo-implementation
```

merge request в ветку main

через интерфейс gitlab'a идем репо далее раздел code - merge requests - create merge request
