"""Выведите на печать пространство всех имён, определённых
в экземпляре класса Cat.
(Класс Cat создан в предыдущем задании.
Импортируйте его в новый модуль,
создайте экземпляр этого класса
и выполните это задание.)

"""

from practicum_14_1 import Cat

matroskin = Cat("Matroskin")

print(matroskin.__dir__())

# Кот Рыжик ест.
# Кот Рыжик бегает.
# Собака Шарик ест.
# Собака Шарик ест.
# ['name', '__module__', '__init__', 'eat', 'run', '__dict__', '__weakref__', '__doc__', '__new__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__reduce_ex__', '__reduce__', '__getstate__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
