"""1. Дано предложение из слов, разделенных пробелами.
Написать функцию transform(), которая принимает такое предложение и возвращает аналогичное,
но где все слова длины 3 в этом предложении - заглавными буквами.

Пример:
“The quick brown fox jumps over the lazy dog” -> “THE quick brown FOX jumps over THE lazy DOG”.
"""


def transform(text: str) -> str:
    return ' '.join([e.upper() if len(e) == 3 else e for e in text.split()])


sentence = "The quick brown fox jumps over the lazy dog"
result = transform(sentence)
print(result)  # THE quick brown FOX jumps over THE lazy DOG

""" =============================================================================================
2. Изменим условие 1 задачи:
нужно, чтобы функция из примера 1 могла также менять слова длины 4 на написанные маленькими буквами.
В общем виде, нужно, чтобы функции можно было дать условие, которому соответствует указанное действие.

Например, все слова длины 4 хотим заменить на звёздочки.
А слова длины 2 - на чёрточки.
Каждое выполнение функции - одно условие и одно действие.
"""


def transform_1(n_law: list, text: str = '') -> str:
    new_words = []
    words = text.split()

    for word in words:
        len_word = len(word)
        func_lst = [f for n, f in n_law if len_word == n]  # [lambda w: w.upper()]
        if func_lst:
            func = func_lst[0]
            new_word = func(word)
        else:
            new_word = word
        new_words.append(new_word)

    return ' '.join(new_words)


sentence = "The quick brown fox jumps over the lazy dog"
res = transform_1(
    [
        (3, lambda w: w.upper()),
        (4, lambda w: '_'.join(list(w))),
        (5, lambda w: '*****'),
    ],
    text=sentence
)
print(res)


def transform_2(n_law: list, text: str = '') -> str:
    new_words = []
    words = text.split()

    for word in words:
        new_word = word
        len_word = len(word)
        for n, f in n_law:
            if len_word == n:
                new_word = f(word)
        new_words.append(new_word)

    return ' '.join(new_words)


sentence = "The quick brown fox jumps over the lazy dog"
res = transform_2(
    [
        (3, lambda w: w.upper()),
        (4, lambda w: '_'.join(list(w))),
        (5, lambda w: '*****'),
    ],
    text=sentence
)
print(res)

""" =============================================================================================
3. Подумайте, как уменьшить количество кода в решении задачи 2, например,
избавившись от явных циклов и использовать python comprehension вместо них.
"""


def transform_3(n_law: list, text: str = ''):
    return ' '.join(next((f(w) for n, f in n_law if len(w) == n), w) for w in text.split())


sentence = "The quick brown fox jumps over the lazy dog"
res = transform_3(
    [
        (3, lambda w: w.upper()),
        (4, lambda w: '_'.join(list(w))),
        (5, lambda w: '*****'),
    ],
    text=sentence
)
print(res)

""" ===================================================================================================
4. Есть магазин по продаже мороженого. Одна порция стоит 5 евро.
В кассе на момент открытия магазина - 0 евро.
В магазин выстраивается очередь покупателей, у которых есть одна купюра, чтобы оплатить порцию мороженого.

Задача: зная купюры всех покупателей в очереди (конечного размера), понять, получится ли продать мороженое всем
(для этого надо иметь достаточно купюр, чтобы давать сдачу), или не получится.

Существуют купюры следующего номинала: 5, 10, 20, 50 евро.
Напишите функцию, которая принимает список с купюрами покупателей.
Например, если очередь имеет купюры [5, 10, 5, 20], то функция вернет true
(первому покупателю продадут мороженое за 5,
со второго возьмут 10 и дадут сдачу 5,
третьему дадут мороженое за 5,
с четвертого возьмут 20 евро и дадут сдачу 15 купюрами 10 и 5 которые есть в кассе).

Подсказка: кассу можно представить в виде списка, отсортированного по возрастанию.
Когда нужно понять, можно ли дать сдачу, то мы перебираем список кассы и суммируем банкноты в нём.
Если они могут в сумме дать сдачу, то мы их убираем из списка, добавляем банкноту,
которой платили, пересортировываем, и так далее).
"""
from bisect import insort


def is_change_exist(cashbox: list, change: int) -> bool:
    if sum(cashbox) < change:
        return False

    for i in range(len(cashbox) - 1, -1, -1):  # проверяем купюры в касе, начиная с самых больших
        if change - cashbox[i] == 0:  # если купюра равна сдаче
            cashbox.pop(i)  # забираем купюру и заканчиваем проверку кассы
            return True
        elif change - cashbox[i] < 0:  # если купюра больше нужной сдачи
            continue  # переходим к следующей в кассе
        else:  # если купюра меньше нужной сдачи
            change -= cashbox[i]  # уменьшаем сдачу, забрав из кассы купюру
            cashbox.pop(i)
    return not change  # если сдача равна нулю, значит мы нашли в кассе нужное количество купюр для нее


def can_sell_icecream(queue: list[int]) -> bool:
    cashbox = []  # касса
    for banknote in queue:
        ch = banknote - 5  # сдача с банкноты
        if is_change_exist(cashbox, ch):  # если есть сдача, забираем ее с кассы
            insort(cashbox, banknote)  # кладём в кассу банкноту покупателя в порядке возрастания
        else:
            return False
    return True


print(can_sell_icecream([5, 10, 10]))  # False
print(can_sell_icecream([5, 5, 10, 10]))  # True
print(can_sell_icecream([5, 10, 5, 20]))  # True
print(can_sell_icecream([50, 10, 5, 20, 10, 10, 5, 5, 5]))  # False
print(can_sell_icecream([50, 10, 5, 20, 10, 10, 5, 5, 5, 5]))  # False
