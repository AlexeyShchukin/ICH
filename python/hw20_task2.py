def count_unique_chars(s: str) -> int:
    chars = {}
    for char in s:
        chars[char] = chars.get(char, 0) + 1
    return len(chars)


print(f"Number of unique characters: {count_unique_chars(input('Enter a string: '))}")
