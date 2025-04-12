from functools import reduce
from itertools import accumulate

nums = [int(num) for num in input('Enter numbers separated by spaces: ').split()]
list_product = reduce(lambda x, y: x * y, nums)
print(f"The product of numbers: {list_product}")
acc_list = list(accumulate(nums, lambda x, y: x * y))
print(f'The list of products of numbers: {acc_list}')
