def get_value_from_dict(d: dict, k):
    if input('Use the get method? (y/n): ') == 'y':
        return d.get(k)
    return d.setdefault(k)


# def get_dict():
#     n = int(input('Enter a number of keys for your dictionary: '))
#     d = {}
#     for i in range(1, n + 1):
#         key = input(f'Enter the {i} key: ')
#         d[key] = input(f'Enter the value of the {i} key: ')
#     return d


# my_dict = get_dict()
# search_key = input('Enter search key: ')
# print(f'The value of key {search_key}: {get_value_from_dict(my_dict, search_key)}')

example = {'apple': 5, 'banana': 6, 'cherry': 7}
target = 'banana'
print(f'The value of key {target}: {get_value_from_dict(example, target)}')
