class Calculator:

    def sum_nums(self, a, b):
        return a + b

    def sub_nums(self, a, b):
        return a - b

    def prod_nums(self, a, b):
        return a * b

    def div_nums(self, a, b):
        if b == 0:
            return 'На ноль делить нельзя'
        return a / b

    def div_rest(self, a, b):
        if b == 0:
            return 'На ноль делить нельзя'
        return a % b

    def num_power(self, a, b):
        return a ** b


if __name__ == '__main__':
    calculator = Calculator()
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    print("Сумма:", calculator.sum_nums(a, b))
    print("Разность:", calculator.sub_nums(a, b))
    print("Произведение:", calculator.prod_nums(a, b))
    print("Частное:", calculator.div_nums(a, b))
    print("Остаток от деления:", calculator.div_rest(a, b))
    print("Первое число в степени второго числа:", calculator.num_power(a, b))
