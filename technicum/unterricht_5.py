import math

"""Aufgabe 1 Einführung in OOP
Erstellen Sie eine Klasse Kreis mit dem Attribut Radius und Methoden zur Berechnung des Umfangs und der Fläche
des Kreises. Das Programm sollte ein Objekt der Klasse erstellen und die Ergebnisse der Berechnungen ausgeben."""

class Circle:
    def __init__(self, radius: float, name: str):
        """
        Wir initialisieren einen Kreis mit dem Attribut Radius
        """
        self.radius = radius
        self.name = name

    def calculate_circumference(self) -> float:
        """
        Umfang berechnen: 2 * pi * radius
        """
        return 2 * math.pi * self.radius

    def calculate_area(self) -> float:
        """
        Flache berechnen: pi * radius^2
        """
        return math.pi * (self.radius ** 2)


c1 = Circle(5, 'kreisli')
res1 = c1.calculate_circumference()
res2 = c1.calculate_area()

print(round(res1, 2), round(res2, 2), c1.name, sep="\n")

"""Aufgabe 2: KlassenmethodenSchreiben Sie eine Klasse Zaehler, die eine Klassenmethode enthält, 
die die Anzahl der erstellten Objekte dieser Klasse zurückgibt. Erstellen Sie mehrere Objekte und 
überprüfen Sie, ob die Methode die Anzahl korrekt zurückgibt."""


class Zahler:
    count = 0

    def __init__(self):
        Zahler.count += 1

    @classmethod
    def get_count(cls):
        """ Anzahl der erstellten Objekte als Ausgabe """
        return cls.count


# Nun erstellen wir Objekte vom Typ Zahler
zahler1 = Zahler()
zahler2 = Zahler()
print(Zahler.get_count())

"""Aufgabe 3: Dekoratoren
Erstellen Sie einen Dekorator, der die Anzahl der Aufrufe der dekorierten Funktion zählt. Wenden Sie diesen Dekorator
auf eine Funktion an, die eine Willkommensnachricht für den Benutzer ausgibt."""


def my_decorator(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count

        res = func(*args, **kwargs)
        count += 1
        print(f'Nach der Funktion {count}')
        return res

    return wrapper


@my_decorator
def input_user(name: str):
    return name


for i in range(10):
    input_user('Oliver')

"""Aufgabe 4: Magische Methoden
Schreiben Sie eine Klasse Vektor, die die Operationen Addition, Subtraktion und Multiplikation mit einem Skalar
unterstützt, indem die entsprechenden magischen Methoden überladen werden. Testen Sie die Klasse mit
verschiedenen Beispielen.
"""


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, scalar: float):
        return Vector(self.x + scalar, self.y + scalar, self.z + scalar)

    def __sub__(self, scalar: float):
        return Vector(self.x - scalar, self.y - scalar, self.z - scalar)

    def __rsub__(self, scalar: float):
        return Vector(scalar - self.x, scalar - self.y, scalar - self.z)

    def __mul__(self, scalar: float):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __truediv__(self, scalar: float):
        return Vector(self.x / scalar, self.y / scalar, self.z / scalar)

    def __rtruediv__(self, scalar: float):
        return Vector(scalar / self.x, scalar / self.y, scalar / self.z)

    def __str__(self):
        return f'{vars(self)}'


v1 = Vector(3, 4, 5)

res = v1 - 1  # lsub
res1 = 1 - v1  # rsub
res2 = v1 * 3
res3 = v1 / 2
res4 = 10 / v1

print(res, res1, res2, res3, res4, sep="\n")
