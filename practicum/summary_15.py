"""Создать класс животных, имеющий атрибут species,
и далее создать объекты этого класса:
3 вида животных - собака, кошка и лошадь.
(Animal -> dog, cat, horse)
Не забудьте при выводе экземпляра класс на печать отобразить значение его атрибутов.
"""


class Animal:
    def __init__(self, species):
        self.species = species

    def __repr__(self):
        return f"{self.__class__.__name__}(species={self.species})"


dog = Animal('dog')
cat = Animal('cat')
horse = Animal('horse')

print(dog)
print(cat)
print(horse)

# Animal(species=dog)
# Animal(species=cat)
# Animal(species=horse)


""" 02 ========================================================
Создайте класс Car для представления автомобиля.
Класс должен иметь атрибуты brand (марка) и model (модель),
которые передаются в конструкторе при создании экземпляра класса.
Реализуйте метод __str__, который будет возвращать строку
в формате "Марка: <марка>, Модель: <модель>".

Ожидаемый вывод:

Марка: Toyota, Модель: Camry
Марка: BMW, Модель: X5
"""


class Car:
    count = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.count += 1

    def __str__(self):
        return f"Марка: {self.brand}, Модель: {self.model}"


""" 03 ========================================================
Добавьте счётчик количества выпущенных с конвейера автомобилей count,
который должен увеличиваться на 1
при создании очередного экземпляров класса.
"""

print(f"Всего выпущено автомобилей: {Car.count}")

car1 = Car("Toyota", "Camry")
print(car1)
print(f"Всего выпущено автомобилей: {Car.count}")

car2 = Car("BMW", "X5")
print(car2)
print(f"Всего выпущено автомобилей: {Car.count}")

# 0
# Марка: Toyota, Модель: Camry
# 1
# Марка: BMW, Модель: X5
# 2
