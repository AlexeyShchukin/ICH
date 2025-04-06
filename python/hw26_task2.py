# 2. Напишите программу, которая принимает в качестве аргумента командной
# строки путь к директории и выводит список всех файлов и поддиректорий внутри этой директории.
# Для этой задачи используйте модуль os и его функцию walk.
# Программа должна выводить полный путь к каждому файлу и директории.

from sys import argv
from os import walk


def dir_parce(dir_path):
    res = []
    for path, dirs, files in walk(dir_path):
        res += [path + '/' + dir_name for dir_name in dirs]
        res += [path + '/' + file_name for file_name in files]
    return res


if len(argv) != 2:
    print("Use: python <script_name.py> <path_to_dir>")

print(dir_parce(argv[1]))
