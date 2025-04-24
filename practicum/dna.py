from itertools import zip_longest


class DNA:
    def __init__(self, sequence):
        self.sequence = sequence
        self.length = len(sequence)
        self.nucleotides = []

    def __str__(self):
        return f"DNA({self.sequence})"

    def __add__(self, other):
        if isinstance(other, DNA):
            return DNA("".join(((x or "") + (y or "") for x, y in zip_longest(self.sequence, other.sequence))))
        return NotImplemented
