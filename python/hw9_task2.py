s = input('Enter a string: ').lower()
vowels = 'aeiou'
idx = 0
s_vowels = 0
s_spaces = 0
while idx < len(s):
    if s[idx] == ' ':
        s_spaces += 1
    elif s[idx] in vowels:
        s_vowels += 1
    idx += 1
print(f'''Number of vowels: {s_vowels}
Number of consonants: {len(s) - s_vowels - s_spaces}''')


