def sum_digits_non_tail(n):
    if n < 10:
        return n
    return n % 10 + sum_digits_non_tail(n // 10)


def sum_digits_tail(n, accumulator=0):
    if n < 10:
        return accumulator + n
    return sum_digits_tail(n // 10, accumulator + n % 10)


a = 12345
print("Сумма цифр: ", sum_digits_non_tail(a)) # 15
print("Сумма цифр: ", sum_digits_tail(a)) # 15


def fact_non_tail(n):
    if n == 0:
        return 1
    return n * fact_non_tail(n - 1)


def fact_tail(n, accumulator=1):
    if n == 0:
        return accumulator
    return fact_tail(n - 1, accumulator * n)


N = 5
print(f"{N}! = {fact_non_tail(N)}")
print(f"{N}! = {fact_tail(N)}")