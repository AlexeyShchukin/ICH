try:
    f = open("nums.txt", 'r')
except FileNotFoundError as e:
        print(f'{e.__class__.__name__}: Invalid path or file name')
else:
    a, b = f.read().strip().split()
    try:
        c = int(a) / int(b)
    except ValueError as e:
        print(f'{e.__class__.__name__} These are not integers')
    except ZeroDivisionError as e:
        print(f'{e.__class__.__name__}: Division by zero is not allowed')
    except Exception as e:
        print(f'2. {e.__class__.__name__}: {e}')
    else:
        print(c)
    finally:
        f.close()
