"""Создать класс Car (машина) со следующими полями: model, year, color."""


class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def __repr__(self):
        return f"{self.__class__.__name__}(model={self.model}, year={self.year}, color={self.color})"

    def __str__(self):
        return self.__repr__()


"""02 ===============================================
Создайте список из 10 объектов этого класса,
описывающих модели разных марок, лет и цветов.
Используйте для этого следующие данные:
"""

data = [
    ('Golf', 2020, 'Red'),
    ('Toyota', 2019, 'Blue'),
    ('Polo', 2021, 'Green'),
    ('Alfa-Romeo', 2018, 'Black'),
    ('Skoda', 2022, 'Red'),
    ('Touareg', 2017, 'Yellow'),
    ('Sharan', 2016, 'Red'),
    ('Phaeton', 2015, 'Gold'),
    ('BMV', 2014, 'Brown'),
    ('Nissan', 2013, 'Red')
]

cars = [Car(brand, year, color) for brand, year, color in data]

"""03 ================================================
Написать функцию get_cars_by_color(), которая принимает
список объектов класса Car и цвет и возвращает iterator объект машин этого цвета.

Напечатать этот список, выводя название модели, год и цвет.
Использовать filter и lambda функции.
"""
from typing import Iterator, List


def get_cars_by_color(vehicles: List[Car], color: str) -> Iterator[Car]:
    return filter(lambda x: x.color == color, cars)


red_cars = get_cars_by_color(cars, "Red")
for car in red_cars:
    print(car)
# Car(brand=Golf, year=2020, color=Red)
# Car(brand=Golf, year=2020, color=Red)
# Car(brand=Skoda, year=2022, color=Red)
# Car(brand=Sharan, year=2016, color=Red)
# Car(brand=Nissan, year=2013, color=Red)


""" 04-05 ==========================================================
Создать класс Person с полями имя и дата рождения (формат str).
Создать класс Employee который содержит поле имя и возраст (int)


Создать 10 объектов класса Person с разными именами.

Написать функцию, которая
    из списка объекта класса Person старше 18 лет
    создаёт список из объектов класса Employee,
    вычисляя возраст каждого Person по дате рождения.

Используя map и filter, попробуйте реализовать трансформации 
списка Person в список Employee в одну строчку.

Вывести получившихся сотрудников на экран.

Используя функцию all() убедиться, что все сотрудники действительно старше 18 лет.
"""
from datetime import datetime


class Person:
    def __init__(self, name: str, birth_day: str):
        self.name = name
        self.birth_day = birth_day

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, birth_day={self.birth_day})"

    def __str__(self):
        return self.__repr__()

    def get_age(self):
        birthdate = datetime.strptime(self.birth_day, '%Y-%m-%d').date()
        today = datetime.today().date()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age


class Employee:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, age={self.age})"

    def __str__(self):
        return self.__repr__()


persons = [
    Person("Ivan", '2020-04-17'),
    Person("Alex", '1987-07-18'),
    Person("Bob", '1994-01-20'),
    Person("Jack", '1999-11-04'),
    Person("Mike", '2002-03-11'),
    Person("Anton", '2007-05-03'),
    Person("Lola", '2014-12-27'),
    Person("Leyla", '2010-09-13'),
    Person("Anna", '1980-10-23'),
    Person("Maxim", '1985-03-10')
]

employees = map(lambda x: Employee(x.name, x.get_age()), filter(lambda x: x.get_age() >= 18, persons))

for person in employees:
    print(person)

print(all(person.age >= 18 for person in employees))
