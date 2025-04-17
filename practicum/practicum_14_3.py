"""Создать класс Person с атрибутами
    - имя,
    - дата рождения,
    - рост (в метрах)
    - вес (в килограммах)
    и методами для вычисления
        - возраста
                birth_day = "2000-01-30"
                birthdate = datetime.strptime(birth_day, '%Y-%m-%d').date()
                today = datetime.today().date()
                age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        - индекса массы тела
                BMI = weight / (height ** 2)

Рост и вес при создании класса являются необязательными.
Если хотя бы один из этих параметров отсутствует - индекс массы тела возвращает None
Создать конструкторы от разного числа аргументов.
Переопределить методы __str__, __repr__.
"""

from datetime import datetime


class Person:
    def __init__(self, name: str, birth_day: str, height: int | None = None, weight: int | None = None):
        self.name = name
        self.birth_day = birth_day
        self.height = height
        self.weight = weight

    def __repr__(self):
        return (f"{self.__class__.__name__}({self.name}, "
                f"{self.birth_day}, "
                f"{self.height}, "
                f"{self.weight})")

    def __str__(self):
        return (f"{self.__class__.__name__}(name={self.name}, "
                f"birth_day={self.birth_day}, "
                f"height={self.height}, "
                f"weight={self.weight})")

    def get_age(self):
        birthdate = datetime.strptime(self.birth_day, '%Y-%m-%d').date()
        today = datetime.today().date()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age

    def get_bmi(self):
        if self.weight is not None:
            return self.weight / (self.height ** 2)


person1 = Person('Alice', '1990-05-15')
person2 = Person('Bob', '1985-05-15', 1.75, 70)

print(person1)
print(repr(person1))
print(f"Возраст {person1.name}: {person1.get_age()} лет")
print(f"BMI {person1.name}: {person1.get_bmi()}")

print(person2)
print(repr(person2))
print(f"Возраст {person2.name}: {person2.get_age()} лет")
print(f"BMI {person2.name}: {person2.get_bmi():.2f}")

# Person(name=Alice, birth_year=1990, height=None, weight=None)
# Person('Alice', 1990, None, None)
# Возраст Alice: 34 лет
# BMI Alice: None

# Person(name=Bob, birth_year=1985, height=1.75, weight=70)
# Person('Bob', 1985, 1.75, 70)
# Возраст Bob: 39 лет
# BMI Bob: 22.86
