def func(students: list, threshold: int):
    return [name for name, age, grade in students if grade > threshold]


arr = [("Alice", 20, 90), ("Bob", 19, 80), ("Charlie", 21, 95), ("David", 18, 85)]
num = int(input('Enter the GPA threshold: '))
print(f'Students with a GPA above {num}: {func(arr, num)}')
