"""С помощью функции count_vowels необходимо написать функцию list_transform,
которая из списка слов создаёт новый список количества гласных в этих словах.
И выводит полученный список на печать в виде строки, разделённой пробелами.
Вывод: vowels_in_words = [2, 3, 3]
Функцию count_vowels необходимо импортировать из предыдущего модуля.
"""

from text_verification import count_vowels


def list_transform(word_list):
    vowels = []
    for word in word_list:
        vowels.append(count_vowels(word))
    return vowels


if __name__ == '__main__':
    words = ['apple', 'orange', 'banana']
    print(list_transform(words))
