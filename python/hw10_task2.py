# check for all characters including spaces
s = input('Введите строку: ')
temp = ''
i = 0
repeated = ''

while i < len(s):
    if s[i] not in temp:
        temp += s[i]
    elif s[i] in temp and s[i] not in repeated:
        repeated += s[i]
    i += 1

if repeated == '':
    print('All characters in the string are unique.')
elif len(repeated) == 1:
    print(f"The character '{repeated}' is repeated.")
else:
    print(f"The characters '{"', '".join(repeated[:-1])}' and '{repeated[-1]}' are repeated.")
