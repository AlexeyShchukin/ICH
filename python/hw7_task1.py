n = int(input('Enter a natural decimal number: '))
res = ''
while n:
    res = str(n % 2) + res
    n = n // 2
print(res)
