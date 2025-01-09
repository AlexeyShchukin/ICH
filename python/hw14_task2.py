num = input("Enter a number (or 'Exit' to finish): ")
res = []
while num != 'Exit':
    res.append(num)
    num = input("Enter a number (or 'Exit' to finish): ")
print(f'Dynamic array: {list(map(lambda x: int(x), res))}')
