n = int(input('Enter a positive integer: '))
x = 2
flag = True
while x < n:
    if n % x == 0:
        flag = False
        break
    x += 1
print(f'The number {n} {"is" if flag else "is not"} a prime number')
