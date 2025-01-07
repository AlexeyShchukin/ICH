n = int(input('Enter a number: '))
print('Multiplication table:')
for i in range(1, n + 1):
    print()
    for j in range(1, n + 1):
        print(str(i * j).ljust(3), end=' ')
