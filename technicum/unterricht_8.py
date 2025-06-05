# Aufgabe 5.
# Erstellen Sie eine Klasse Animal mit den Feldern: Name und Geburtsdatum.
# Erstellen Sie eine Klasse Pet mit den Feldern: Name und Alter in "Tierjahren"
# (wobei 1 Menschenjahr 7 Tierjahren entspricht). Schreiben Sie eine Funktion,
# die eine Liste von Animal-Objekten in eine Liste von Pet-Objekten umwandelt,
# indem sie das Alter jedes Tieres basierend auf seinem Geburtsdatum berechnet.
# Behalten Sie nur die Tiere, die älter als 2 Jahre in "Tierjahren" sind.

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_pet(self):
        return Pet(self.name, self.age)


class Pet:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        if self._age > 2:
            return self._age * 7
        return self._age

    def __repr__(self):
        return f'Pet: {self.name}, age: {self.age}'



animals = [Animal('Tom', 5), Animal('Jerry', 2)]

pets = [animal.to_pet() for animal in animals]

print(pets)




