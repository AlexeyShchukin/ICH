"""Напишите программу, выводящую следующий список:
['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
Последний элемент списка состоит из 26 символов z.
"""


def alphabet():
    res = []
    for i in range(1, 27):
        res.append(chr(96 + i) * i)
    return res


print(alphabet())
print('zzzzzzzzzzzzzzzzzzzzzzzzzz'.count('z'))
