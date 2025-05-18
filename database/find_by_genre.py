from database.local_settings import HOST, USER, PASSWORD, SAKILA
from mysql.connector import connect

dbconfig = {
    'host': HOST,
    'user': USER,
    'password': PASSWORD,
    'database': SAKILA,
}


def get_film_by_actor():
    genre = input("Enter the genre of films you want: ").title()
    year = input("Enter the year of films you want: ")
    print(f"=====Searching {genre} movies released in {year}=====")
    with connect(**dbconfig) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """SELECT title FROM film f 
                JOIN film_category fc ON f.film_id = fc.film_id
                JOIN category c ON fc.category_id = c.category_id 
                WHERE c.name LIKE %s AND f.release_year = %s;""", (f'%{genre}%', year,)
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