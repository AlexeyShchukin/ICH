"""Написать класс Circle, который
    - задаёт круг по радиусу
    и может вычислять
        - площадь get_area()
        - и длину окружности get_circumference()
    а также имеет методы:
        - __str__()
        - __repr__()

PI определить как атрибут класса, равное 3.1415926535
"""


class Circle:
    PI = 3.1415926535

    def __init__(self, r):
        self.r = r

    def __repr__(self):
        return (f"{self.__class__.__name__}(\"{self.r}\")")

    def __str__(self):
        return (f"Circle with radius {self.r}")

    def get_area(self):
        return self.__class__.PI * self.r ** 2

    def get_circumference(self):
        return 2 * self.__class__.PI * self.r


circle3 = Circle(3)

print(circle3)
print(repr(circle3))
print(f"Area of a circle: {circle3.get_area():.2f}")
print(f"Circumference: {circle3.get_circumference():.2f}")

# Circle with radius 3
# Circle("3")
# Area of a circle: 28.27
# Circumference: 18.85
