with open('nums.txt', 'r', encoding='utf-8') as file:
    try:
        a, b = [int(num) for num in file.readline().strip().split()]
        c = a / b
        if c < 0:
            raise ValueError('The number must be positive')
        else:
            print(c)
    except ValueError as e:
        print(f'1. {e.__class__.__name__}: {e}')
    except Exception as e:
        print(f'2. {e.__class__.__name__}: {e}')

