"""В базе данных ich_edit три таблицы:
    Users с полями (id, name, age),
    Products с полями (pid, prod, quantity) и
    Sales с полями (sid, id, pid).

Дан список с именами таблиц.
Программа должна в цикле сделать запрос к каждой из указанных таблиц.
Если таблица есть в базе - вывести на печать её содержимое.
Если нет - вывести сообщение:"The table {table_name} does not exist!"
"""

from mysql.connector import connect
from local_settings import HOST, USER, PASSWORD, DATABASE

dbconfig = {
    'host': HOST,
    'user': USER,
    'password': PASSWORD,
    'database': DATABASE,
}

with connect(**dbconfig) as conn:
    with conn.cursor() as cursor:
        tables = ['Users', 'Products', 'Sales']
        try:
            for table in tables:
                cursor.execute(f"SELECT * FROM {table}")
                print(f"===== Table '{table}': =====")
                print(cursor.fetchall())
        except Exception as e:
            print(e)
