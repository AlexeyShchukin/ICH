def sort_nums(a, b, c):
    if a < b < c:
        print(a, b, c)
    elif b < a < c:
        print(b, a, c)
    elif c < a < b:
        print(c, a, b)
    elif a < c < b:
        print(a, c, b)
    elif b < c < a:
        print(b, c, a)
    else:
        print(c, b, a)


if __name__ == '__main__':
    sort_nums(int(input('Введите первое число: ')),
              int(input('Введите второе число: ')),
              int(input('Введите третье число: ')))
