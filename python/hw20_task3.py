from statistics import mean


def calculate_average_grade(students: dict) -> dict:
    avg_grades = {}
    for k, v in students.items():
        avg_grades[k] = round(mean(v), 2)
    return avg_grades


def get_dict():
    n = int(input('Enter number of students: '))
    grades = {}
    for _ in range(n):
        name = input('Enter student name: ')
        grades[name] = [int(grade) for grade in input('Enter grades separated by spaces: ').split()]
    return grades


print(calculate_average_grade(get_dict()))
