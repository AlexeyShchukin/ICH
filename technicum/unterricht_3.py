"""Schreiben Sie ein Programm, das eine Zeichenkette vom Benutzer abfragt. Das Programm soll die Häufigkeit jedes
Zeichens in der Zeichenkette zählen und die Ergebnisse in einem Wörterbuch speichern, wobei der Schlüssel das
Zeichen und der Wert die Häufigkeit seines Vorkommens ist."""

line = "Hello world!!!"
my_dict = {}

for c in line:
    my_dict[c] = my_dict.get(c, 0) + 1

print(my_dict)

# Die zweite Lösung
from collections import defaultdict

d = defaultdict(int)
for c in line:
    d[c] += 1

print(dict(d))
