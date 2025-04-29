"""Создайте класс Book с приватными атрибутами (__private)
    author (автор)
    title (название)
Реализуйте доступ к этим атрибутам через геттеры и сеттеры.

Далее необходимо создать класс-метод
    - create_book(title, author), который принимает название книги и её автора
                                  и возвращает экземпляр класса Book.

Не забудьте также реализовать метод __str__
"""


class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def __str__(self):
        return f'Book "{self.__title}" by {self.__author}'

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value

    @classmethod
    def create_book(cls, title, author):
        return cls(title, author)


if __name__ == '__main__':
    book1 = Book.create_book("Leo Tolstoy", "War and Peace")
    book2 = Book.create_book("Jane Austen", "Pride and Prejudice")

    print(book1)
    print(book2)

# Book War and Peace by Leo Tolstoy
# Book Pride and Prejudice by Jane Austen
