from time_counter import time_counter


@time_counter
def bubble_sort(arr: list):
    n = len(arr)
    for i in range(n - 1):
        flag = True
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                flag = False
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if flag:
            break
    return arr


if __name__ == '__main__':
    print(bubble_sort([1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6, 8, -2, 99]))
