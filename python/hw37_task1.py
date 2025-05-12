"""В базе данных ich_edit три таблицы. Users с полями (id, name, age),
Products с полями (pid, prod, quantity) и Sales с полями (sid, id, pid).

Программа должна запросить у пользователя название таблицы и
вывести все ее строки или сообщение, что такой таблицы нет."""
from mysql.connector import connect, Error

from database.local_settings import dbconfig

table = input("Enter table name: ")

try:
    with connect(**dbconfig) as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {table}")
            print(*cursor.fetchall(), sep='\n')
except Error as e:
    print(f"{e.__class__.__name__}: {e}")
