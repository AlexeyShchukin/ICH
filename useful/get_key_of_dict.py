from typing import Hashable, Any, Dict


def get_key(d: Dict[Hashable, Any], value: Any) -> Hashable | None:
    for k, v in d.items():
        if v == value:
            return k
    return None


hashmap = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
target = 3
print(get_key(hashmap, target))
