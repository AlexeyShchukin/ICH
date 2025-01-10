class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum_nums(self):
        return self.a + self.b

    def sub_nums(self):
        return self.a - self.b

    def prod_nums(self):
        return self.a * self.b

    def div_nums(self):
        if self.b == 0:
            return 'Division by zero is impossible'
        return self.a / self.b

    def div_rest(self):
        if self.b == 0:
            return 'Division by zero is impossible'
        return self.a % self.b

    def num_power(self):
        return self.a ** self.b


if __name__ == '__main__':
    calculator = Calculator(float(input('Enter first number: ')), float(input('Enter second number: ')))
    print("Sum:", calculator.sum_nums())
    print("Difference:", calculator.sub_nums())
    print("Product:", calculator.prod_nums())
    print("Quotient:", calculator.div_nums())
    print("Remainder from division:", calculator.div_rest())
    print("The first number to the power of the second number:", calculator.num_power())
