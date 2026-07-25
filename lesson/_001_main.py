import pandas as pd

# from sqlalchemy import create_engine

# # Созданный дата фрейм
# sales_data = pd.DataFrame(
#     {
#         "manager": [
#             "Иван",
#             "Мария",
#             "Петр",
#             "Анна",
#             "Сергей",
#             "Иван",
#             "Мария",
#             "Анна",
#             "Ольга",
#         ],
#         "department": ["А", "Б", "А", "В", "Б", "А", "Б", "В", "А"],
#         "revenue": [15000, 22000, 17000, 12000, 25000, 18000, 19000, 14000, 16000],
#         "experience": [2, 5, 3, 1, 4, 2, 5, 1, 2],
#         "period": ["Q1", "Q1", "Q1", "Q1", "Q1", "Q2", "Q2", "Q2", "Q2"],
#     }
# )

# Чтение данных из Excel файла
df_csv = pd.read_csv(
    "/home/nvmaxim/Projects/dev-sandbox/lesson/data/sales_data.csv",
    sep=";",
)
df = df_csv


# # Подключение к SQL
# def connect_to_postgres():
#     DB_CONFIG = {
#         "host": "localhost",  # тот же хост, что в SQL Tools
#         "port": "5432",  # тот же порт
#         "database": "study",  # имя БД из вашего скриншота
#         "user": "postgres",  # имя пользователя
#         "password": "4470",  # ваш пароль от PostgreSQL
#     }

#     # Создаем строку подключения
#     connection_string = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"

#     # Подключаемся к БД
#     engine = create_engine(connection_string)
#     return engine


# # 🔍 ПОКАЗЫВАЕМ ДАННЫЕ ИЗ БД
# try:
#     # Подключаемся к БД
#     engine = connect_to_postgres()
#     print("✅ Успешное подключение к PostgreSQL!")

#     # 📋 1. ПОКАЗАТЬ ВСЕ ТАБЛИЦЫ В БАЗЕ
#     print("\n" + "=" * 50)
#     print("1. ВСЕ ТАБЛИЦЫ В БАЗЕ ДАННЫХ:")

#     tables_query = """
#     SELECT table_name
#     FROM information_schema.tables
#     WHERE table_schema = 'public'
#     """
#     tables = pd.read_sql(tables_query, engine)
#     print(tables)

#     # 📊 2. ПОКАЗАТЬ ДАННЫЕ ИЗ ТАБЛИЦЫ sales_data
#     print("\n" + "=" * 50)
#     print("2. ДАННЫЕ ИЗ ТАБЛИЦЫ sales_data:")

#     # Просто читаем всю таблицу
#     sales_data_from_db = pd.read_sql("SELECT * FROM sales_data", engine)
#     df = sales_data_from_db
#     print("Все данные из таблицы:")
#     print(sales_data_from_db)
# finally:
#     if "engine" in locals():
#         engine.dispose()
