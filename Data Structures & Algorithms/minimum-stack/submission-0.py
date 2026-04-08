class MinStack:

    def __init__(self):
        self.container = list()
        self.min_s = list()

    def push(self, val: int) -> None:
        self.container.append(val)
        if self.min_s == []:
            self.min_s.append(val)
        else:
            self.min_s.append(min(val, self.min_s[-1]))

    def pop(self) -> None:
        self.min_s.pop()
        return self.container.pop()

    def top(self) -> int:
        return self.container[-1]

    def getMin(self) -> int:
        return self.min_s[-1]
