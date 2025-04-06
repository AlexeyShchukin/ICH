# 1. Напишите программу, которая принимает в качестве аргумента командной строки путь к файлу .py и запускает его.
# При запуске файла программа должна выводить сообщение "Файл <имя файла> успешно запущен".
# Если файл не существует или не может быть запущен, программа должна вывести соответствующее сообщение об ошибке.

from sys import argv
from os import path
from subprocess import run


def run_file(file_path):
    if path.exists(file_path) and file_path.endswith('.py'):
        try:
            run(['python', file_path], check=True)
            print(f"File {file_path} successfully launched.")
        except Exception as e:
            print(f"{e.__class__.__name__}: {e}")
    else:
        print(f"File {file_path} does not exist or is not a Python file.")


if len(argv) != 2:
    print("Use: python <script_name.py> <path_to_file.py>")

run_file(argv[1])
