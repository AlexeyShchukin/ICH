from database.local_settings import HOST, USER, PASSWORD, SAKILA
from mysql.connector import connect

dbconfig = {
    'host': HOST,
    'user': USER,
    'password': PASSWORD,
    'database': SAKILA,
}


def get_film_by_actor():
    actor = input("Enter the actor name of films you want: ").upper()
    print(f"=====Searching for film with actor {actor}=====")
    with connect(**dbconfig) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """SELECT title FROM film f 
                JOIN film_actor fa ON f.film_id = fa.film_id
                JOIN actor a ON fa.actor_id = a.actor_id 
                WHERE CONCAT(a.first_name, ' ', a.last_name) LIKE %s;""", (f'%{actor}%',)
            )
            films = cursor.fetchall()
            if not films:
                print("No films found with that keyword.")
            else:
                total = len(films)
                for i in range(0, total, 10):
                    chunk = films[i:i + 10]
                    for title in chunk:
                        print(title[0])
                    if i + 10 < total:
                        cont = input("Continue? (Press Enter to continue, any other key to stop): ")
                        if cont.strip() != '':
                            break


get_film_by_actor()