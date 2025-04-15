class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def calculate_area(self):
        return self.width * self.height


if __name__ == '__main__':
    rectangle = Rectangle(width=int(input('Enter the width: ')), height=int(input('Enter the height: ')))
    print(f'The area of {rectangle!r}: {rectangle.calculate_area()}')
