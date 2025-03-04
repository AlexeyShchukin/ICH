"""01 Дано натуральное число N.
Выведите все числа от 1 до N используя рекурсию.

* Попробуйте выполнить решение в двух вариантах: для хвостовой, и НЕ хвостовой рекурсии?
"""
from itertools import accumulate


def tail_recursion(n, current=1):
    if current <= n:
        print(current)
        tail_recursion(n, current + 1)


tail_recursion(5)


def non_tail_recursion(n):
    if n == 1:
        print(n)
        return
    non_tail_recursion(n - 1)
    print(n)


non_tail_recursion(5)

"""02 ===================================
Дано натуральное число N (1, 2, 3 ...).
Написать функцию power_of_2(N), которая
    - печатает слово YES, если число N является точной степенью двойки
      (2^0 = 1,
       2^1 = 2,
       2^2 = 4,
       2^3 = 8 и так далее)
    - или слово NO в противном случае.

Пользуемся рекурсией, а операцией возведения в степень не пользуемся.

Пример:
    power_of_2(8) вернет YES,
    power_of_2(1) вернет YES.
    power_of_2(3) вернет NO.
"""


def power_of_2(n, accumulator=0):
    if 2 ** accumulator == n:
        print('YES')
        return
    elif 2 ** accumulator > n:
        print('NO')
        return
    else:
        power_of_2(n, accumulator + 1)


power_of_2(8)  # YES
power_of_2(1)  # YES
power_of_2(3)  # NO

"""03 ====================================
Дано натуральное число N.
Написать функцию digits_sum(N), которая вычисляет сумму его цифр.
При решении этой задачи пользуемся рекурсией, а строки, списки, массивы и циклы не используем.
Пример digits_sum(179) = 17
"""


def digits_sum_non_tail(n):
    if n == 0:
        return n
    return n % 10 + digits_sum_non_tail(n // 10)


print(digits_sum_non_tail(179))  # 17


def digits_sum_tail(n, accumulator=0):
    if n:
        accumulator += n % 10
        return digits_sum_tail(n // 10, accumulator)
    return accumulator


print(digits_sum_tail(179))  # 17

"""04 ==================================================
Дано слово, состоящее только из строчных латинских букв.
Проверьте с помощью рекурсии, является ли это слово палиндромом.
Выведите YES или NO.

Пример:
    is_palindrome("radar") вернёт Yes
    is_palindrome("abba")) вернёт Yes
    is_palindrome("yes"))  вернёт No
"""


def is_palindrome(word):
    if len(word) <= 1:
        return 'Yes'
    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return 'No'


print(is_palindrome("radar"))  # Yes
print(is_palindrome("abba"))  # Yes
print(is_palindrome("yes"))  # No

"""05 ==========================================================
C клавиатуры вводится последовательность целых чисел, заканчивающаяся числом 0.
Выведите эту последовательность в обратном порядке.
При решении этой задачи нельзя пользоваться массивами и прочими динамическими структурами данных,
а нужно пользоваться рекурсией.
"""


def reverse_sequence():
    num = int(input())
    if num == 0:
        print(num)
        return
    reverse_sequence()
    print(num)


reverse_sequence()
# 3
# 2
# 1
# 0
# 0 1 2 3


"""06 ======================================================
Напишите функцию, которая получает на вход три слова и определяет,
являются ли они анаграммами друг друга.
Использовать множества.
Важное ограничение: известно, что буквы в пределах одного слова не повторяются.
Функция возвращает:
 - True, если слова являются анаграммами и
 - False в противном случае.

Пример:
is_anagram(“кластер”, “стрелка”, “сталкер”) = True.
"""


def is_anagram(word1, word2, word3):
    return set(word1) == set(word2) == set(word3)


print(is_anagram("кластер", "стрелка", "сталкер"))  # True

print(is_anagram("вольер", "собака", "пример"))  # False

"""07 =====================================================
На входе функция to_set() получает строку или список чисел.
Преобразуйте их в множество.
На выходе должно получиться множество и его мощность (cardinality).
"""


def to_set(seq: list | str) -> tuple[set, int]:
    hashset = set(seq)
    return hashset, len(hashset)


print(to_set([1, 2, 3, 4, 5]))  # ({1, 2, 3, 4, 5}, 5)
print(to_set("cardinality"))  # ({'y', 'r', 'a', 'c', 'i', 't', 'l', 'd', 'n'}, 9)

"""08 ==========================================
Предоставлен список натуральных чисел.
Требуется сформировать из них множество.
Если какое-либо число повторяется, то преобразовать его в строку по образцу:
например, если число 4 повторяется 3 раза, то в множестве будет следующая запись:
    - само число 4;
    - строка 44 (второе повторение, т.е. число дублируется в строке);
    - строка 444 (третье повторение, т.е. строка множится на 3).

Реализуйте вывод множества через функцию set_gen().
"""


def set_gen(nums: list[int]) -> set[int | str]:
    hashset = set()
    for num in nums:
        counter = nums.count(num)
        if counter > 1:
            for i in range(2, counter + 1):
                hashset.add(str(num) * i)
        hashset.add(num)

    return hashset


print(set_gen([1, 1, 1, 2, 2, 3]))  # {1, 2, 3, '111', '22', '11'}

print(set_gen([1, 1, 1, 2, 2, 3]) == {1, 2, 3, '111', '22', '11'})  # True

"""09 ==========================================
Напишите функцию, которая получает на вход
    две строки с перечислением интересов и хобби двух пользователей, и
    вычисляет процент совпадения.

Процент рассчитывается, как отношение числа совпадений к максимальному числу интересов
ОДНОГО ИЗ участников.
(например: у 1-го - 3 хобби, у 2-го - 4 хобби
=> max будет равен 4)

Использовать множества.
"""


def match_percentage(interests_1: str, interests_2: str) -> float:
    set1 = set(interests_1.split(', '))
    set2 = set(interests_2.split(', '))
    max_length = max(len(set1), len(set2))
    return len(set1 & set2) / max_length * 100


user1_interests = "путешествия, фотография, кино, музыка"
user2_interests = "фотография, кино, литература, спорт"

result = match_percentage(user1_interests, user2_interests)
print(f"Процент совпадения интересов: {result:.2f} %")

"""Напиши рекурсивную функцию sum_nested(lst), которая принимает список, в котором элементы могут быть либо числами, 
либо другими списками (вложенными на произвольную глубину). Функция должна возвращать сумму всех чисел, 
содержащихся в этом списке."""


def sum_nested(lst: list, accumulator=0) -> int:
    for e in lst:
        if isinstance(e, int):
            accumulator += e
        else:
            accumulator += sum_nested(e)
    return accumulator


arr = [1, 2, [3, 4], [5, [6, 7]], 8]
print(sum_nested(arr))
# Сумма: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36
