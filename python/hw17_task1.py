def modify_list(arr: list):
    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            arr[i] *= 2
        else:
            arr[i] = int(arr[i] / 2)


if __name__ == '__main__':
    my_list = [int(e) for e in input('Enter a list of numbers separated by spaces: ').split()]
    modify_list(my_list)
    print(f'Modified list of numbers: {my_list}')
