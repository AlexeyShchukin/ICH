def is_hashable(obj):
    try:
        hash(obj)
    except Exception as e:
        print(f'{e.__class__.__name__}: {e}')
        return False
    return True


print(is_hashable([]))