# Вернуть список, с перемещенными нулями вконец.

def move_zeros(arr: list) -> list:
    return sorted(arr, key=lambda x: x == 0)


print(move_zeros([1, 2, 3, 0, 4, -1, 0, -5, -3, 0, 4, 10]))
