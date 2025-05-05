import re

"""Написать программу, которая использует функции языка для работы
с регулярными выражениями и синтаксис регулярных выражений:
"""

text = """In 2025, cybersecurity matters more than ever. Passwords like "P@ssw0rd123
or "Z!9gT#4q" aren't secure. Use phrases: "Myd0g$Jumps#High!". Avoid using names, 
birthdays (e.g., 12/03/1990), or simple patterns like "abcd1234". Enable 2FA — codes 
like 742981 or apps like Authy help. Never share login links via email (phishing!). 
Encrypt data with AES-256. Backup files weekly to ... Consider password managers 
(e.g., Bitwarden, 1Password). Update software regularly — version 3.5.1 > 3.4.9. Use VPNs, 
avoid public Wi-Fi. Stay alert, check URLs (https://secure-site.com vs http://fake-site.ru). 
Cyber hygiene saves time, money, and stress. Be smart, be safe — your digital life depends on it."""

"1. Определите, содержит ли заданная строка набор данных символов (a-z, A-Z и 0-9)."
match = re.search(r"\w+", text)
print(bool(match))

"2. Определите, содержит ли строка символ ‘a’, за которым следует ноль или более символов ‘b’"
match2 = re.search(r"ab*", text)
print(bool(match2))

"3. Определите, содержит ли строка символ ‘a’, за которым следует 1 или более символов ‘b’"
match3 = re.search(r"ab+", text)
print(bool(match3))

"4. Определите, содержит ли строка символ ‘a’, за которым следует 0 или 1 символ ‘b’."
match4 = re.search(r"ab?", text)
print(bool(match4))

"5. Определите, содержит ли строка символ z."
match5 = re.search(r"z", text)
print(bool(match5))

"6. Определите, содержит ли строка только буквы, цифры и символ подчеркивания."
match6 = re.search(r"\w", text)
print(bool(match6))

"7. Определите, начинается ли строка с заданного числа."
match7 = re.search(r"^007", text)
print(bool(match7))

"""8. Напишите программу, которая удаляет нули (0) перед цифрами в IP адресе.
    Например, “192.01.001.10”  → “192.1.1.10”"""

match8 = re.sub(r"\b0+(\d+)", r"\1", "0192.01.001.010")
print(match8)

"9. Определите, содержит ли строка цифры в конце."
match9 = re.search(r"\d$", text, re.M)
print(bool(match9))

"""10. Найдите вхождения и позиции подстроки в строке.
    Пример: строка “Домашние задания, задания в классе, отпускные задания”,
    подстрока “задания”,
    вывод “задания” на 9:16, “задания” на 18:25, “задания” на 46:53."""

s = "Домашние задания, задания в классе, отпускные задания"
target = r"задания"
matches = re.finditer(target, s)
for match in matches:
    print(f"{target} на {match.start()}:{match.end()}")

"11. Напишите программу, которая заменяет пробелы подчёркиваниями и обратно."
print(re.sub(r" ", "_", text))
print(re.sub(r"_", " ", text))

"""12. Частью URL часто является дата в формате 2016/09/02.
    Например, https://www.somesite.com/news/2024/01/22/article.html.
    Найдите все даты в URL такого вида.
    Вывод может выглядеть так [('2024', '01', '22')]."""

url = "https://www.somesite.com/news/2024/01/22/article.html"
date_data = re.findall(r"(\d{4})/(\d{2})/(\d{2})", url)
print(date_data)

"13. Напишите программу, которая конвертирует дату в формате yyyy-mm-dd в формат dd-mm-yyyy."

date_en = "2024-01-22"
converted_date = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3-\2-\1", date_en)
print(converted_date)

"""14. Напишите программу, которая отделяет и печатает цифры в заданной строке.
    Например, для строки "Ten 10, Twenty 20, Thirty 30" должно быть выведено 10, 20, 30."""

s = "Ten 10, Twenty 20, Thirty 30"
digits = re.finditer(r"\d+", s)
print(*(digit.group(0) for digit in digits), sep=", ")

"""15. Напишите программу, которая выводит все слова,
    начинающиеся на букву ‘a’ и ‘e’ в заданном предложении."""

pattern = r"\b[ae][a-zA-Z]+"
res = re.findall(pattern, text)
print(*res)

"16. Напишите программу, которая печатает цифры и их позиции в заданной строке текста."

s = "Ten 10, Twenty 20, Thirty 30"
pattern = r"(\d)"
matches = re.finditer(pattern, s)
for match in matches:
    print(f"digit = {match.group()}, pos = {match.start()}")

"""17. Напишите программу, которая сокращает Strasse на Str. в заданной строке,
    например, “Flensburger Strasse” → “Flensburger Str.”."""

s = "Flensburger Strasse"
match = re.sub(r"Strasse", "Str.", s)
print(match)

"18. Напишите программу, которая заменяет все вхождения пробела, запятой или точки подчеркиванием."

s = "Напишите программу, которая заменяет все вхождения пробела, запятой или точки подчеркиванием."
print(re.sub(r"[,. ]", "_", s))

"19. Напишите программу, которая находит все слова длины 3 в заданном предложении."

s = "Все слова ищу, где три буквы."
print(*re.findall(r"\b[а-яА-Я]{3}\b", s))

"""20. Напишите программу, которая находит все слова длины 3, 4 и 5 символов
    в заданном предложении."""

s = "Find all words with 3-5 characters"
print(*re.findall(r"[a-zA-Z]{3,5}", s))

"""21. Напишите программу, которая превращает camel-case строку в snake-case строку,
    например, “ПайтонПрограммист” -> “пайтон_программист”."""

s = """Напишите программу, которая превращает camel-case строку в snake-case строку,
    например, “ПайтонПрограммист” -> “пайтон_программист”."""
print(re.sub(r"([а-яА-Я]+)([А-Я])+", r"\1_\2", s).lower())

"""22. Напишите программу, которая выводит значения между кавычками в строке.
    Например, "Python", "PHP", "Java" -> [‘Python’, ‘PHP’, ‘Java’]."""

s = '"Python", "PHP", "Java"'
print(re.findall(r'"(\w+)"', s))

"""23. Напишите программу, которая удаляет несколько идущих подряд пробелов из строки,
    заменяя их одним пробелом. “Hello     World” -> “Hello World”."""

s = "“Hello     World” -> “Hello World”."
print(re.sub(r" +", " ", s))

"24. Напишите программу, которая удаляет все пробелы из строки."

print(re.sub(" +", "", s))

"""25. Напишите программу, которая заменяет в тексте все слова,
    начинающиеся на ‘х’ или ‘f’ на звёздочки."""

text = """Foxes are fast and clever animals. The forest is full of sounds and shadows. 
In some areas, you might spot an old fax machine or a forgotten file. 
Xylophones echo faintly through the mist, while xenon lights flicker in the dark."""

print(re.sub(r"\b[xf][a-z]+", lambda x: len(x.group(0)) * '*', text))
