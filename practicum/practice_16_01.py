"""Создайте абстрактный базовый класс Car и его дочерние классы WV и Toyota.
Определите необходимые атрибуты и методы для каждого класса.
Реализуйте методы, проверяющие работу созданных классов.

Абстрактный класс Car:
    Атрибуты:
        brand (марка автомобиля)
        model (модель автомобиля)
        year (год выпуска автомобиля)
    Методы:
        start_engine: метод выводит сообщение о запуске двигателя
            "Engine for car model WV Passat is started"
            ВАЖНО: этот метод НЕ переопределяется в дочерних классах!
        print_color: абстрактный метод, который должен быть переопределён в дочерних классах
            "The color for this model WV Passat is red."
Дочерние классы содержат дополнительный атрибут color (цвет)
"""

from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        return f"Engine for car model {self.brand} {self.model} is started"

    @abstractmethod
    def print_color(self):
        return f"The color for this model {self.brand} {self.model} is "


class WV(Car):
    def __init__(self, brand, model, year, color):
        super().__init__(brand, model, year)
        self.color = color

    def print_color(self):
        return super().print_color() + self.color


class Toyota(Car):
    def __init__(self, brand, model, year, color):
        super().__init__(brand, model, year)
        self.color = color

    def print_color(self):
        return f"The color for this model {self.brand} {self.model} is {self.color}."


wv = WV('WV', 'Passat', 2024, 'red')
print(wv.start_engine())
print(wv.print_color())

t = Toyota('Toyota', 'Camry', 2024, 'green')
print(t.start_engine())
print(t.print_color())

# Engine for car WV model Passat is started
# The color for this model WV Passat 2024 is red.
# Engine for car model Toyota Camry is started
# The color for this model WV Passat 2024 is green.
