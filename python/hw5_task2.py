def bissextile(year: int):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


if __name__ == '__main__':
    year = int(input('Enter year: '))
    print(f'The year {"is" if bissextile(year) else "is not"} a leap year.')
