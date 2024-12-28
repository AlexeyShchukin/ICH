n = int(input('Введите число N: '))
prev_num = 0
next_num = 1
idx = 0
while idx < n:
    print(prev_num, end=', ' if idx < n - 1 else '')
    prev_num, next_num = next_num, prev_num + next_num
    idx += 1
