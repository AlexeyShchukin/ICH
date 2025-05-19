"""Verwenden Sie collections.Counter, um die Anzahl jedes Zeichens in einer Zeichenkette zu zählen. Schreiben Sie
eine Funktion count_characters, die eine Zeichenkette annimmt und ein Counter Objekt mit der Anzahl der
einzelnen Zeichen zurückgibt. Geben Sie anschließend die 3 am häufigsten vorkommenden Zeichen aus.
"""
from collections import Counter, deque, namedtuple
from math import dist


def count_characters(s: str):
    return Counter(s).most_common(3)


print(count_characters("fastretrewgr"))

"""Verwenden Sie collections.deque, um eine Warteschlange mit fester Länge zu erstellen. Schreiben Sie eine
Funktion fixed_queue, die eine Liste von Zahlen und die maximale Länge der Warteschlange annimmt, die
Elemente der Liste zur Warteschlange hinzufügt und den endgültigen Zustand der Warteschlange zurückgibt"""


def fixed_queue(liste: list, max_length: int):
    q = deque(maxlen=max_length)
    for num in liste:
        q.append(num)
    return list(q)


def fixed_queue1(liste: list, max_length: int):
    return deque(liste[: max_length])


print(fixed_queue([1, 4, 5, 6, 2, 7, 3, ], 5))
print(fixed_queue1([1, 4, 5, 6, 2, 7, 3, ], 5))

"""Erstellen Sie ein benanntes Tupel Point mit den Feldern x, y und z. Schreiben Sie eine Funktion calculate_distance,
die zwei Point Objekte annimmt und den Abstand zwischen ihnen im dreidimensionalen Raum berechnet."""

Point = namedtuple("Point", ["x", "y", "z"])
point1 = Point(1, 3, 9)
point2 = Point(4, 2, -5)


def calculate_distance(p1, p2):
    return dist(p1, p2)


print(calculate_distance(point1, point2))

"""Schreiben Sie eine Funktion safe_divide, die zwei Zahlen annimmt und das Ergebnis ihrer Division zurückgibt.
Wenn die Division nicht möglich ist Division durch Null), soll die Funktion die Meldung "Cannot divide by zero"
zurückgeben, ohne die Ausführung des Programms zu unterbrechen.
"""


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        return f"{e.__class__.__name__}: Cannot divide by zero"


print(safe_divide(4, 2))
print(safe_divide(4, 0))

"""Schreiben Sie eine Funktion read_file, die versucht, eine Textdatei zu öffnen und zu lesen. Wenn die Datei nicht
existiert, soll die Funktion den Fehler FileNotFoundError behandeln und die Meldung "File not found" ausgeben.
Im Falle anderer Fehler soll die Meldung "An error occurred" ausgegeben werden.
"""


def read_file():
    try:
        with open("file", "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError as e:
        return f"{e.__class__.__name__}: File not found"


print(read_file())

"""Schreiben Sie eine Funktion get_integer, die den Benutzer auffordert, eine Zahl einzugeben. Wenn der Benutzer
keine ganze Zahl eingibt, soll die Funktion die Ausnahme ValueError behandeln und die Eingabe erneut abfragen,
bis ein gültiger Wert eingegeben wird."""


def get_integer(num: float | int) -> int:
    if num % 1 == 0:
        return int(num)
    res = float(input("Geben Sie bitte eine ganze Zahl: "))

    return get_integer(res)


print(get_integer(3.5))
