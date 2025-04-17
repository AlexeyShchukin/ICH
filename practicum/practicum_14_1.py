"""Создайте класс Animal с методами eat() и run().
Наследуйте от него классы Cat и класс Dog.
Эти классы должны иметь
 - атрибут name
 - и методы eat() и run().
При вызове методов eat() и run() соответственно выводится на печать:
"Кот Рыжик ест"
"Кот Рыжик бегает"
"Собака Шарик ест"
"Собака Шарик бегает"
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        ...

    def run(self):
        ...


class Cat(Animal):
    def eat(self):
        print(f"Кот {self.name} ест")

    def run(self):
        print(f'Кот {self.name} бегает')


class Dog(Animal):
    def eat(self):
        print(f"Собака {self.name} ест")

    def run(self):
        print(f'Собака {self.name} бегает')


cat_ryzhik = Cat("Рыжик")
dog_sharik = Dog("Шарик")

cat_ryzhik.eat()
cat_ryzhik.run()
dog_sharik.eat()
dog_sharik.run()

# Кот Рыжик ест.
# Кот Рыжик бегает.
# Собака Шарик ест.
# Собака Шарик бегает.
