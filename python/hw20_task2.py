def count_unique_chars(s: str) -> int:
    chars = {}
    for char in s:
        chars[char] = chars.get(char, 0) + 1  # записываем в хеш таблицу символы с количеством их повторений
    return len(chars)


def count_unique_chars2(s: str) -> int:
    return len(set(s))


print(f"Number of unique characters: {count_unique_chars(input('Enter a string: '))}")
print(f"Number of unique characters: {count_unique_chars2(input('Enter a string: '))}")
