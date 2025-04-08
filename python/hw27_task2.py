def compose_functions(funcs: list, n: int) -> int:
    res = n
    for func in funcs:
        res = func(res)
    return res


add_one = lambda x: x + 1
double = lambda x: x * 2
subtract_three = lambda x: x - 3
functions = [add_one, double, subtract_three]
print(compose_functions(functions, int(input('Enter a number: '))))
