def sum_mtx(matrix: list):
    res = 0
    for row in matrix:
        res += sum(row)
    return res


def get_mtx():
    rows = int(input('Enter the number of rows in the matrix: '))
    cols = int(input('Enter the number of columns in the matrix: '))
    mtx = []
    for i in range(rows):
        while True:
            row = input(f'Row {i + 1}. Enter {cols} numbers separated by space: ').split()
            if len(row) == cols:
                mtx.append([int(num) for num in row])
                break
            else:
                print(f'Error: Need to enter {cols} numbers!')
    return mtx


if __name__ == '__main__':
    print(f'Sum of elements in the matrix: {sum_mtx(get_mtx())}')
