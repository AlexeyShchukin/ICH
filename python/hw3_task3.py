class Distance:
    @staticmethod
    def calculation(x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


if __name__ == '__main__':
    print('Введите координаты первой точки (x1, y1): ')
    x1, y1 = float(input()), float(input())
    print('Введите координаты второй точки (x2, y2): ')
    x2, y2 = float(input()), float(input())
    print(f'Расстояние между точками: {Distance.calculation(x1, y1, x2, y2)}')
