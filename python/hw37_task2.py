"""В базе данных ich_edit три таблицы. Users с полями (id, name, age),
Products с полями (pid, prod, quantity) и Sales с полями (sid, id, pid).

Программа должна вывести все имена из таблицы users, дать пользователю
выбрать одно из них и вывести все покупки этого пользователя."""
from mysql.connector import connect

from database.local_settings import dbconfig

with connect(**dbconfig) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM Users")
        names = [row[1] for row in cursor.fetchall()]
        print("===== Table 'Users': =====")
        print(names)
        user = input("Enter user name: ")
        cursor.execute(
            """SELECT u.name, p.prod FROM Users u
            JOIN Sales s ON u.id = s.id
            JOIN Products p ON s.pid = p.pid
            WHERE u.name = %s""", [user]
        )
        res = cursor.fetchall()
        print(f"===== Purchases of User <{user}> : =====")
        if len(res[0]) == 1:
            print(f"User {user} has no purchases")
        else:
            print(*[e[1] for e in res], sep="\n")
