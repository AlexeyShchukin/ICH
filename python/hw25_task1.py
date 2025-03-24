from typing import List


def find_longest_word(word_list: List[str]) -> str:
    return max(word_list, key=len)


words = input('Enter words separated by spaces: ').split()
result = find_longest_word(words)
print(result)
