# sum of the digits of a number
def sum_digits(num: int):
    if abs(num) < 10:
        return num
    return num % 10 + sum_digits(num // 10)


if __name__ == '__main__':
    number = int(input('Enter a number: '))
    print(f'The sum of the digits of the number {number} is: {sum_digits(number)}')
