from functools import reduce


def sum_square_nums(nums: list) -> int:
    sq_nums = map(lambda x: x ** 2, nums)
    even_sq_nums = filter(lambda x: x % 2 == 0, sq_nums)
    return reduce(lambda x, y: x + y, even_sq_nums)


numbers = list(map(lambda x: int(x), input('Enter numbers: ').split(', ')))
print(f"Result: {sum_square_nums(numbers)}")
