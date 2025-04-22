"""Создать класс Shape, описывающий абстрактную фигуру,
у которой есть площадь. У этого класса есть метод calculate_area(),
который возвращает площадь фигуры.
У класса также есть атрибут экземпляра класса name,
которое содержит строчное название фигуры.
Например, “круг”, “прямоугольник” и так далее.

Метод __str__() должен содержать имя класса,
а также перечень всех атрибутов:
ClassName(attr1=value1, attr2=value2, ...)

Унаследовать от класса Shape 3 других класса:
Circle, Square, Rectangle.
У каждого класса должны быть соответствующие атрибуты,
необходимые для вычисления площади фигуры.

Для каждого класса переопределить метод calculate_area(),
который вычисляет площадь фигуры.
"""
from abc import abstractmethod
from functools import wraps
from math import pi as PI


class Shape:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        attrs = [f"{k}={v}" for k, v in self.__dict__.items()]
        return f"{self.__class__.__name__}({', '.join(attrs)})"

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, name, r):
        super().__init__(name)
        self.r = r

    def calculate_area(self):
        return PI * self.r ** 2


class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def calculate_area(self):
        return self.side ** 2


class Rectangle(Shape):
    def __init__(self, name, side1, side2):
        super().__init__(name)
        self.side1 = side1
        self.side2 = side2

    def calculate_area(self):
        return self.side1 * self.side2


if __name__ == '__main__':
    r = Rectangle("rectangle", 3, 4)
    c = Circle("circle", 3)
    sq = Square("square", 4)

    print(r)
    print(c)
    print(sq)

    print(r.calculate_area())
    print(c.calculate_area())
    print(sq.calculate_area())

    # Rectangle(name=rectangle, side1=3, side2=4)
    # Circle(name=circle, radius=3)
    # Square(name=square, side=4)
    # 12
    # 28.274333882308138
    # 16

""" 02 ======================================================================================================
Импортировать классы фигур из предыдущего файла.

Составить список, содержащий по 2 экземпляра каждого класса фигуры.
Вывести на печать площадь каждого объекта в формате:
Area of Circle(name=circle, radius=5): 78.54
с точностью до 2-го знака после запятой
"""

figures = [
    Circle('circle', 5),
    Circle('circle', 3),
    Square('square', 4),
    Square('square', 6),
    Rectangle('rectangle', 3, 4),
    Rectangle('rectangle', 5, 6)
]

for obj in figures:
    print(f"Area of {obj}: {obj.calculate_area()}")

# Area of Circle(name=circle, radius=5): 78.54
# Area of Circle(name=circle, radius=3): 28.27
# Area of Square(name=square, side=4): 16.00
# Area of Square(name=square, side=6): 36.00
# Area of Rectangle(name=rectangle, side1=3, side2=4): 12.00
# Area of Rectangle(name=rectangle, side1=5, side2=6): 30.00


""" 03 ==============================================================================================================
Существует функция coffee(), которая варит кофе
и если ее вызвать, то она печатает "Сварить кофе"

Создайте 4 декоратора так, чтобы в итоге каждый из них добавлял бы
к слову "кофе" следующие фразы:
    - с сахаром,
    - молоком
    - с сахаром и молоком
    - двойной

Вызов декорируемой функции с декоратором (с декораторами)
в итоге должен выводить печатать то, с чем именно кофе сварено

Сварить кофе двойной с сахаром и молоком
Сварить кофе с сахаром и молоком
Сварить кофе с молоком

и так далее.

Представьте, что у вас есть класс Coffee с полем цена и название. Декорировать этот класс по аналогии с предыдущей задачей, чтобы можно было получить кофе с молоком (стоит дороже), кофе с сахаром (цена остается такой же), двойной кофе (цена удваивается).

"""


def with_sugar(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func()
        print("с сахаром", end=" ")

    return wrapper


def with_milk(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func()
        print("с молоком", end=" ")

    return wrapper


def with_sugar_and_milk(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func()
        print("с сахаром и молоком", end=" ")

    return wrapper


def double_coffee(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func()
        print("двойной", end=" ")

    return wrapper


@with_milk
@double_coffee
def coffee1():
    print("Сварить кофе", end=" ")


@with_sugar
@double_coffee
def coffee2():
    print("Сварить кофе", end=" ")


@with_sugar_and_milk
def coffee3():
    print("Сварить кофе", end=" ")


coffee1()
print()

coffee2()
print()

coffee3()
print()

# Сварить кофе двойной с молоком
# Сварить кофе двойной с сахаром
# Сварить кофе с сахаром и молоком


""" 04 ======================================================================================================
Представьте, что у вас есть класс Coffee с атрибутами
    - цена и
    - название.

Декорировать этот класс по аналогии с предыдущей задачей,
чтобы можно было получить кофе с молоком (стоит дороже),
кофе с сахаром (цена остаётся такой же), двойной кофе (цена удваивается).
"""


class Coffee:
    def __init__(self, price, name):
        self.price = price
        self.name = name

    def __str__(self):
        return f"{self.name} (price: {self.price} euro)"


def WithSugar():
    def decorator(cls):
        class Wrapped(cls):
            def __init__(self, price, name):
                super().__init__(price, name + " with sugar")

            def __str__(self):
                return f"{self.name} (price: {self.price} euro)"

        return Wrapped

    return decorator


def WithMilk():
    def decorator(cls):
        class Wrapped(cls):
            def __init__(self, price, name):
                super().__init__(price + 2, name + " with milk")

            def __str__(self):
                return f"{self.name} (price: {self.price} euro)"

        return Wrapped

    return decorator


def DoubleCoffee():
    def decorator(cls):
        class Wrapped(cls):
            def __init__(self, price, name):
                super().__init__(price * 2, "Double " + name)

            def __str__(self):
                return f"{self.name} (price: {self.price} euro)"

        return Wrapped

    return decorator


@WithSugar()
class CoffeeWithSugar(Coffee):
    pass


@WithMilk()
class CoffeeWithMilk(Coffee):
    pass


@WithMilk()
@WithSugar()
class CoffeeWithSugarAndMilk(Coffee):
    pass


@DoubleCoffee()
class DoubleCoffeeCup(Coffee):
    pass


@WithMilk()
@DoubleCoffee()
class DoubleCoffeeWithMilk(Coffee):
    pass


# Coffee
coffee = Coffee(3, "Coffee")
print(coffee)
# Coffee (price: 3 euro)

# Coffee with suger
coffee_with_sugar = CoffeeWithSugar(3, "Coffee")
print(coffee_with_sugar)
# Coffee with sugar (price: 3 euro)

# Coffee with milk
coffee_with_milk = CoffeeWithMilk(3, "Coffee")
print(coffee_with_milk)
# Coffee with milk (price: 5 euro)

# Coffee with suger and milk
coffee_with_sugar_and_milk = CoffeeWithSugarAndMilk(3, "Coffee")
print(coffee_with_sugar_and_milk)
# Coffee with milk with sugar (price: 5 euro)

# Double coffee
double_coffee_cup = DoubleCoffeeCup(3, "Coffee")
print(double_coffee_cup)
# Double Coffee (price: 6 euro)

# Double coffee with milk
double_coffee_with_milk = DoubleCoffeeWithMilk(3, "Coffee")
print(double_coffee_with_milk)
# Double Coffee with milk (price: 10 euro)
