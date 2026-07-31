from airflow.models import DagBag


def test_dagbag_imports():
    """проверка всех dag'ов на наличие ошибок синтаксиса и импорта"""
    dagbag = DagBag(include_examples=False)
    assert len(dagbag.import_errors) == 0, (
        f"ошибки при импорте DAG: {dagbag.import_errors}"
    )
