"""Aufgabe 1: Grundlagen der Arbeit mit Python
Schreiben Sie ein Programm, das zwei Zahlen vom Benutzer entgegen nimmt und grundlegende mathematische
Operationen durchführt: Addition, Subtraktion, Multiplikation, Division, Ganzzahldivision und Potenzieren.
Geben Sie die Ergebnisse im Format "Operation: Ergebnis" aus."""

num1 = float(input("Bitte schreiben Sie eine Zahl: "))  # Werte vom Typ String = Zeichenkette (Deutsch)
num2 = float(input("Schreiben Sie bitte eine zweite Zahl: "))


def addition(a: float, b: float) -> float:
    return a + b


def subtraction(a: float, b: float) -> float:
    return a - b


def multiplication(a: float, b: float) -> float:
    return a * b


def division(a: float, b: float) -> float:
    return a / b


def floor_division(a: float, b: float) -> float:
    return a // b


def power(a: float, b: float) -> float:
    return a ** b


def main():
    print(f"Addition: {addition(num1, num2)}")
    print(f"Subtraktion: {subtraction(num1, num2)}")
    print(f"Multiplikation: {multiplication(num1, num2)}")
    print(f"Division: {division(num1, num2)}")
    print(f"Ganzzahldivision: {floor_division(num1, num2)}")
    print(f"Potenzieren: {power(num1, num2)}")


main()

"""Aufgabe 2:

Aufgabe 2: Operatoren und Ausdrücke
Erstellen Sie ein Programm, das die Summe und das Produkt der Ziffern einer zweistelligen Zahl berechnet, 
die der Benutzer eingegeben hat. 
Verwenden Sie den Modulo-Operator und die Ganzzahldivision, um die Ziffern zu extrahieren."""


def two_digit_operations(num):
    x = num // 10
    y = num % 10
    print(f"Mein Produkt: {x * y}. Meine Summe: {x + y}")


two_digit_operations(int(input("Geben Sie bitte eine zweistellige Zahl ein: ")))


"""Aufgabe 3: Boolesche Datentypen und Vergleiche
Schreiben Sie ein Programm, das prüft, ob man aus drei vom Benutzer 
eingegebenen Zahlen a, b und c ein rechtwinkliges Dreieck bilden kann. 
Das Programm soll True oder False als Ergebnis ausgeben."""

def right_triangle(a: int, b: int, c: int) -> bool:
    return a ** 2 + b ** 2 == c ** 2


lst = [6, 8, 10]
print(right_triangle(*lst))


"""Aufgabe 4: Bedingungsoperator if
Schreiben Sie ein Programm, das eine Bewertung des Benutzers (eine ganze Zahl von 1 bis 5) 
entgegen nimmt und den entsprechenden Text ausgibt: "Sehr schlecht" für 1, "Schlecht" für 2, 
"Befriedigend" für 3, "Gut" für 4, "Sehr gut" für 5.
# if statements benutzen, theoretisch if-else
# Tipp: Dictionary (Wörterbuch benutzen), .get(), my_dict[x]"""

my_dict = {
1: "Sehr schlecht",
2: "Schlecht",
3: "Befriedigend",
4: "Gut",
5: "Sehr gut",
}

def get_grade_from_dict(user_grade:int)->str:
    return my_dict.get(user_grade, "Ich kenne diese Note nicht")

if __name__ == '__main__':
    num = int(input("Bitte nur ganze, positive Zahlen zwischen 1-5 eingeben: "))
    print(get_grade_from_dict(num))


"""Aufgabe 5: Schleife while
Schreiben Sie ein Programm, das eine Zahl vom Benutzer abfragt und alle ihre 
Teiler unter Verwendung einer while-Schleife ausgibt."""

def user_input():
    try:
        n = int(input('Bitte geben Sie eine ganze Zahl ein: \n'))
        return n
    except ValueError:
        return user_input()

def find_factor(my_num=1):
    i=my_num/2
    count=1
    # Starte die Division bei x / 2 und gehe dann herunter
    while (count<=(my_num/2)):
        if my_num % count == 0:
            #print(count)
            print(f'{count} x {my_num/count}')
        count+=1
    print(my_num)

def main():
    n = user_input()
    print(f'Die Teiler/Faktoren von {n} sind: \n\n')
    find_factor(n)
    print('\n\n')

main()