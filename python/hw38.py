"""Доработать мини-интерфейс к базе данных, который был сделан на занятии.
Новые возможности интерфейса:

1. Ввести список полей выбранной таблицы.
2. При вводе искомого значения добавить возможность выбора знака -
найти записи, в которых выбранное поле больше, меньше или равно введенному значению."""

from mysql.connector import connect, Error

from database.local_settings import dbconfig


def get_tables_info(
        tables: list,
        join_cols: list[tuple] = None,
        requested_fields: list[str] = None,
        filter_fields: list[str] = None,
        operators: list[str] = "=",
        values: list[str] = None,
):
    try:
        with connect(**dbconfig) as conn:
            with conn.cursor() as cursor:
                requested_fields = ", ".join(requested_fields) if requested_fields else "*"
                if not join_cols or len(tables) == 1:
                    query = f"""SELECT {requested_fields} FROM {tables[0]}"""
                else:
                    query = f"SELECT {requested_fields} FROM {tables[0]}"
                    for i in range(1, len(tables)):
                        t1 = tables[i - 1]
                        t2 = tables[i]
                        col = join_cols[i - 1]
                        query += f" LEFT JOIN {t2} ON {t1}.{col[0]} = {t2}.{col[1]}"
                if filter_fields:
                    query += f" WHERE {filter_fields[0]} {operators[0]} {int(values[0]) if values[0].isdigit() else values[0]}"
                    if len(filter_fields) > 1:
                        for i in range(1, len(filter_fields)):
                            query += f" AND {filter_fields[i]} {operators[i]} {int(values[i]) if values[i].isdigit() else values[i]}"
                cursor.execute(query)
                return cursor.fetchall()
    except Error as e:
        print(f"{e.__class__.__name__}: {e}")


print(get_tables_info(["Users"]))
print(get_tables_info(
    ["Users", "Sales", "Products"],
    [("id", "id"), ("pid", "pid")],
    ["Sales.sid", "Users.name", "Products.prod", "Products.quantity"],
    ["Products.quantity"],
    ["<"],
    ["12"]
))
