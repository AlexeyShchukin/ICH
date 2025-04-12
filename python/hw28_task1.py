def func(words: list):
    vowels = 'aeiouAEIOU'
    return list(map(lambda x: x.upper(), [word for word in words if word[0] in vowels]))


my_list = input('Enter words separated by spaces: ').split()
print(f"New list: {func(my_list)}")
