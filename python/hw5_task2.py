def bissextile(year: int):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print('Год является високосным.')
    else:
        print('Год не является високосным.')


if __name__ == '__main__':
    bissextile(int(input('Введите год: ')))
