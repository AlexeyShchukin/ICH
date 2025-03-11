from collections import Counter, defaultdict
from pprint import pprint
import json

text = """
В качестве текста использовать текст этой задачи. 

Необходимо посчитать сколько раз встретилось каждое слово и вывести в топ слов, 
упорядоченный сначала по убыванию встречаемости, 
а при равенстве частот в соответствии с упорядочиванием в лексикографическом порядке. 

Слова должны быть переведены в нижний регистр и из них должны быть удалены все небуквенные символы.

Решить задачу с помощью использования изученных классов.
"""


def words_dict_sort(s: str):
    new = ''
    for c in s.lower():
        if c.isalpha() or c == ' ' or c == '\n':
            new += c
    return sorted(Counter(new.split()).items(), key=lambda x: (-x[1], x[0]))


pprint(words_dict_sort(text))

""" 01 ===========================================================================
Словарь синонимов.
Вам дан словарь, состоящий из пар слов.
Каждое слово является синонимом к парному ему слову.
Все слова в словаре различны.
Написать функцию, которая для заданного слова из словаря, определяет его синоним.

Пример словаря:
    dct = {"Hello": "Hi", "Bye": "Goodbye", "List": "Array"}

    get_synonym(“Goodbye”) -> Bye.
    get_synonym(“Plate) -> THe word <Plate> was not found in the dictionary!
"""


def get_synonym(synonyms: dict, word: str) -> str:
    if word in synonyms:
        return synonyms[word]
    for k, v in synonyms.items():
        if word == v:
            return k
    return 'Word <Plate> was not found in the dictionary!'


words = {"Hello": "Hi", "Bye": "Goodbye", "List": "Array"}

print(get_synonym(words, "Goodbye"))  # Bye
print(get_synonym(words, "List"))  # Array
print(get_synonym(words, "Plate"))  # Word <Plate> was not found in the dictionary!

""" 02 ===========================================================================

Дан json-файл 'cities-countries.json', в котором
по ключу <Страна> находится строка с названиями городов, разделённых пробелом.

Напишите функцию, которая:
 - считывает данные из файла;
 - по аргументу ГОРОД возвращает
    - либо название страны
    - либо "not found"

which_country("Novgorod") = Russia
which_country("Mumbai") = Not found

"""


def read_json_file(filename: str) -> dict[str, str]:
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def which_country(func, city: str) -> str:
    for k, v in func.items():
        if city in v:
            return k
    return 'Not found'


print(which_country(read_json_file('cities-countries.json'), 'Novgorod'))  # Russia
print(which_country(read_json_file('cities-countries.json'), 'Donetsk'))  # Italy
print(which_country(read_json_file('cities-countries.json'), 'Muhosransk'))  # Not found

""" 03 ==========================================================================="""

"""Дана база данных о продажах некоторого интернет-магазина.
Каждая строка файла 'sales.json' представляет собой запись вида
покупатель-товар-количество, где
    покупатель — имя покупателя (строка без пробелов),
    товар — название товара (строка без пробелов),
    количество — количество приобретенных единиц товара.

Создайте список всех покупателей, а для каждого покупателя подсчитайте количество приобретенных
им единиц каждого вида товаров.
Список покупателей, а также список товаров для каждого покупателя
нужно выводить в лексикографическом порядке.

Данные:
[
    "Alice-apple-5",
    "Alice-orange-3",
    "Bob-apple-2",
    "Bob-banana-7",
    "Alice-banana-2",
    "Charlie-apple-1
]

Пример вывода:
    {'Alice': {'apple': 5, 'banana': 2, 'orange': 3},
     'Bob': {'apple': 2, 'banana': 7},
     'Charlie': {'apple': 1}}
"""


def read_list_from_json_file(filename: str) -> dict[str, str]:
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def process_sales_data(func) -> dict[str, dict[str, int]]:
    res = {}
    for line in func:
        name, title, amount = line.split('-')
        res.setdefault(name, {}).update({title: amount})
    return res


def process_sales_data2(func) -> dict[str, dict[str, int]]:
    res = defaultdict(lambda: defaultdict(int))
    for line in func:
        name, title, amount = line.split('-')
        res[name][title] += int(amount)
    return dict(res)


pprint(process_sales_data(read_list_from_json_file('sales.json')))
pprint(process_sales_data2(read_list_from_json_file('sales.json')))
# {'Alice': {'apple': 5, 'banana': 2, 'orange': 3},
#  'Bob': {'apple': 2, 'banana': 7},
#  'Charlie': {'apple': 1}}


""" 04 ==========================================================================="""

"""Дополните условие предыдущей задачи:
Информацию о продажах необходимо вывести в файл 'sales-by-customers.json'
"""


def read_list_from_json_file2(filename: str) -> dict[str, str]:
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def write_list_from_json_file(filename: str, dct: dict[str, dict[str, int]]) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(dct, file, ensure_ascii=False, indent=4)


def process_sales_data2(read_from_file: str, write_to_file: str) -> None:
    json_obj = read_list_from_json_file2(read_from_file)
    res = {}
    for line in json_obj:
        name, title, amount = line.split('-')
        res.setdefault(name, {}).update({title: amount})
    write_list_from_json_file(write_to_file, res)


process_sales_data2('sales.json', 'sales-by-customers.json')

""" 05 ==========================================================================="""

"""Добавьте к условиям задачи 1 возможность добавления пользователем собственных синонимов."""


def get_synonym2(synonyms: dict, word: str) -> str:
    if word in synonyms:
        return synonyms[word]
    for k, v in synonyms.items():
        if word == v:
            return k
    return 'Word <Plate> was not found in the dictionary!'


dict_synonyms = {"Hello": "Hi", "Bye": "Goodbye", "List": "Array"}
while True:
    new_pair = input("Enter a word and it's synonym separated by space or stop to finish: ")
    if new_pair == 'stop':
        break
    k, v = new_pair.split()
    if k not in dict_synonyms:
        dict_synonyms[k] = v

print(get_synonym2(dict_synonyms, "Goodbye"))  # Bye
print(get_synonym2(dict_synonyms, "List"))  # Array
print(get_synonym2(dict_synonyms, "Plate"))  # Word <Plate> was not found in the dictionary!
