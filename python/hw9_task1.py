s = input('Enter a string: ').lower()
flag = True
symbol = 97
while symbol < 123:
    if not chr(symbol) in s:
        flag = False
        break
    symbol += 1
print('The string is a pangram.' if flag else 'The string is not a pangram.')
