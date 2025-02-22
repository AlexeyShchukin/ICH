try:
    f = open(input("Enter the path to your file: "), 'r')
except FileNotFoundError:
    print('FileNotFoundError: Invalid path or file name')
else:
    a, b = f.read().strip().split()
    try:
        c = int(a) / int(b)
    except ValueError:
        print("ValueError: These are not integers")
    except ZeroDivisionError:
        print('ZeroDivisionError: Division by zero is not allowed')
    else:
        print(c)
    finally:
        f.close()
