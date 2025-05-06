def shaker_sort(l: list):
    n = len(l)
    for i in range(n // 2):
        flag = True
        for j in range(i, n - 1 - i):
            if l[j] > l[j + 1]:
                flag = False
                l[j], l[j + 1] = l[j + 1], l[j]
        if flag:
            break
        flag = True
        for j in range(n - 2 - i, i, -1):  # от предпоследнего элемента минус i
            # с каждым проходом будем останавливаться на один элемент раньше
            # верхняя же границе i, на первом проходе нулевой элемент не включается, но при сравнении
            # мы берем элемент j, который равен i, и j-1. Таким образом включаем нулевой элемент
            if l[j] < l[j - 1]:
                flag = False
                l[j], l[j - 1] = l[j - 1], l[j]
        if flag:
            break
    return l

if __name__ == '__main__':
    print(shaker_sort([1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6, 8, -2, 99]))
