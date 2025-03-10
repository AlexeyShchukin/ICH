"""2. Напишите программу, которая создает именованный кортеж Person для хранения информации о человеке,
включающий поля name, age и city. Создайте список объектов Person и выведите информацию о каждом человеке на экран.

Пример вывода:
Name: Alice, Age: 25, City: New York
Name: Bob, Age: 30, City: London
Name: Carol, Age: 35, City: Paris"""

from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'city'])
persons = []
persons.append(Person(name='Alice', age='25', city='New York'))
persons.append(Person(name='Bob', age='30', city='London'))
persons.append(Person(name='Carol', age='35', city='Paris'))

# n = int(input('Enter a number of persons: '))
# for i in range(1, n + 1):
#     persons.append(Person(name=input(f'Enter the name of  the {i} person: '),
#                           age=input(f'Enter the age of the {i} person: '),
#                           city=input(f'Enter the city of the {i} person: ')))

for name, age, city in persons:
    print(f'Name: {name}, Age: {age}, City: {city}')
