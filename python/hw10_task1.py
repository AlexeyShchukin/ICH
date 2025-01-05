s = input('Введите строку: ')
vowels = 'aeiouAEIOU'
i = 0
while i < len(vowels):
    s = s.replace(vowels[i], '')
    i += 1
print(s)
