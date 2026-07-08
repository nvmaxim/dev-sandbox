import pandas as pd

# 1. Загружаем файл со штатной расстановкой
# Укажи правильное название файла, если оно отличается
df = pd.read_excel("Штатная расстановка ИЮНЬ.xlsx")

# 2. Убираем лишние пробелы в названиях колонок (частая проблема экселя)
df.columns = df.columns.str.strip()

# 3. Очищаем от пустых строк и вакансий (в дашборде нам нужны только живые люди)
df = df.dropna(subset=["ФИО"])
df = df[~df["ФИО"].str.contains("ВАКАНСИЯ", case=False, na=False)]

# 4. Очищаем сами ФИО от случайных пробелов по краям
df["ФИО"] = df["ФИО"].str.strip()

# 5. Разбиваем ФИО, чтобы вытащить Фамилию в отдельную колонку
# Это нужно для связки (JOIN) с таблицей checkbot.users
fio_split = df["ФИО"].str.split(" ", expand=True)
df["last_name"] = fio_split[0]

# 6. Формируем финальную красивую таблицу для базы данных
final_df = pd.DataFrame(
    {
        "full_name": df["ФИО"],
        "last_name": df["last_name"],
        "department": df["Структурное подразделение"],
        "job_title": df["Должность"],
        "block_name": df["Блок"],
    }
)

# 7. Сохраняем в чистый CSV для DBeaver
final_df.to_csv("clean_org_structure.csv", index=False, encoding="utf-8")
print("Готово! Файл clean_org_structure.csv успешно сохранен и готов к загрузке в БД.")
