class Rectangle:
    def __init__(self, width=3, height=6):
        self.width = width
        self.height = height

    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def __str__(self):
        return f'Rectangle width {self.width} and length {self.height}'

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return (self.width + self.height) * 2


if __name__ == '__main__':
    rectangle = Rectangle()
    print(rectangle)
    print(f'The area of the {rectangle!r}: {rectangle.calculate_area()}')
    print(f'The area of the {rectangle!r}: {rectangle.calculate_perimeter()}')
