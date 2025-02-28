# Отсортируйте список под двум критериям:
# - по длине слова;
# - по длине слова и количеству гласных слове ('aeiouyAEIOUY');
# - по длине и по алфавиту.

words = ["apple", "orange", "banana", "grape", "peach", "melon", "berry", "plum", "kiwi"]
print(sorted(words, key=lambda word: len(word)))
# Сортировка по длине слова:
# ['plum', 'kiwi', 'apple', 'grape', 'peach', 'melon', 'berry', 'orange', 'banana']
# ['plum', 'kiwi', 'apple', 'grape', 'peach', 'melon', 'berry', 'orange', 'banana']

print(sorted(words, key=lambda word: (len(word), len([c for c in word if c in 'aeiouyAEIOUY']))))
# Сортировка по длине слова и количеству гласных слове ('aeiouyAEIOUY'):
# ['plum', 'kiwi', 'apple', 'grape', 'peach', 'melon', 'berry', 'orange', 'banana']
# ['plum', 'kiwi', 'apple', 'grape', 'peach', 'melon', 'berry', 'orange', 'banana']

print(sorted(words, key=lambda word: (len(word), word)))
# Сортировка по длине слова и алфавиту:
# ['kiwi', 'plum', 'apple', 'berry', 'grape', 'melon', 'peach', 'banana', 'orange']



