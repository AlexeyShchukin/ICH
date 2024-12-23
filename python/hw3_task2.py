from math import pi


class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return pi * self.r ** 2

    def circumference(self):
        return 2 * pi * self.r


if __name__ == '__main__':
    circle = Circle(float(input('Введите радиус окружности: ')))
    print(circle.area())
    print(circle.circumference())
