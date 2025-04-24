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
            result = ''.join(a + b for a, b in zip(self.sequence, other.sequence))
            if self.length > other.length:
                result += self.sequence[other.length:]
            else:
                result += other.sequence[self.length:]
            return result
        return NotImplemented
