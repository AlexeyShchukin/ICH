def fibonacci(num: int):
    prev_num = 0
    next_num = 1
    idx = 0
    while idx < num:
        idx += 1
        print(prev_num, end=', ' if idx < num else '\n')
        prev_num, next_num = next_num, prev_num + next_num


if __name__ == '__main__':
    number = int(input('Enter number: '))
    fibonacci(number)
