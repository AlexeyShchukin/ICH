"""Напишите функцию extract_emails(text), которая извлекает все адреса электронной
почты из заданного текста и возвращает их в виде списка."""
from re import findall


def extract_emails(t: str) -> list[str]:
    return findall(r'\w+@\w+.[a-zA-z0-9_]{2,3}', t)


text = "Contact us at info@example.com or support@example.com for assistance."
emails = extract_emails(text)
print(emails)  # Вывод: ['info@example.com', 'support@example.com']
