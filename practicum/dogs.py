""""Написать функцию, которая принимает возраст собаки и возвращает следующую информацию:
["Щенок", "Puppy"]: 	до 1 года включительно;
["Юниор", "Junior"]:  	до 2-х лет включительно;
["Взрослая", "Adult"]: 	до 7-ми лет включительно;
["Старшая", "Senior"]:	до 10-ти лет включительно;
["Гериатрическая", "Geriatric"]:	    старше 10 лет.

Функция также содержит необязательный параметр lang ("en" или "ru"), который определяет язык вывода информации.
По умолчанию lang="en".
Если lang="ru", информацию выводится на русском языке. Для всех остальных вариантов - на английском.
"""


def dog_category(years, lang='en'):
    dogs_list = [["Щенок", "Puppy"], ["Юниор", "Junior"], ["Взрослая", "Adult"],
                 ["Старшая", "Senior"], ["Гериатрическая", "Geriatric"]]
    idx = 0 if lang == 'ru' else 1
    if years <= 1:
        return dogs_list[0][idx]
    elif years <= 2:
        return dogs_list[1][idx]
    elif years <= 7:
        return dogs_list[2][idx]
    elif years <= 10:
        return dogs_list[3][idx]
    return dogs_list[4][idx]


dog_years = int(input('Введите возраст собаки: '))
language = input("Выберите язык ru или en: ")
print(dog_category(dog_years, language))
