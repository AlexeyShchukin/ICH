def merge_dicts(*args):
    res = {}
    for d in args:
        for k, v in d.items():
            res[k] = res.get(k, []) + [v]
    return res


print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}))
