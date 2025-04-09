# Написать стек, который поддерживает push, pop, top, get_min за константное время

class Stack():
    def __init__(self):
        self.stack = []
        self.min_nums = []

    def push(self, num: int):
        self.stack.append(num)
        if not self.min_nums or num <= self.min_nums[-1]:
            self.min_nums.append(num)

    def pop(self):
        res = self.stack.pop()
        if res == self.min_nums[-1]:
            self.min_nums.pop()
        return res

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_nums[-1]
