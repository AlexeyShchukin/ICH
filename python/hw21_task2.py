from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'city'])
persons = []
n = int(input('Enter a number of persons: '))
for i in range(1, n + 1):
    persons.append(Person(name=input(f'Enter the name of  the {i} person: '),
                          age=input(f'Enter the age of the {i} person: '),
                          city=input(f'Enter the city of the {i} person: ')))
for name, age, city in persons:
    print(f'Name: {name}, Age: {age}, City: {city}')
