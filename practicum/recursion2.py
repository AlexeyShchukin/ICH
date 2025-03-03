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


def reverse_sequence2():
    num = int(input())
    if num:
        reverse_sequence()
        print(num)


reverse_sequence()
reverse_sequence2()


"""Это хвостовая рекурсия (tail recursion) или не хвостовая (non-tail recursion)?
Как преобразовать её в рекурсию (не) хвостового типа?
"""


def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])


def sum_list_tail_or_non_tail_recursion(lst, accumulator=0):
    if not lst:
        return accumulator
    return sum_list_tail_or_non_tail_recursion(lst[1:], accumulator + lst[0])


print(sum_list([1, 2, 3, 4, 5]))
print(sum_list_tail_or_non_tail_recursion([1, 2, 3, 4, 5]))  # 15
