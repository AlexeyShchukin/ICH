s = input('Введите строку: ')
width = int(input('Введите ширину: '))
if width % 2 == 0 and len(s) % 2 == 0 or width % 2 == 1 and len(s) % 2 == 1:
    print(s.center(width))
else:
    print(s.rjust(width))
