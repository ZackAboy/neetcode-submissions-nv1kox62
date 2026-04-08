class MyQueue:

    def __init__(self):
        self.inc = list()
        self.out = list()

    def push(self, x: int) -> None:
        self.inc.append(x)

    def transfer(self):
        if not self.out:
            while self.inc:
                self.out.append(self.inc.pop())

    def pop(self) -> int:
        self.transfer()
        return self.out.pop()

    def peek(self) -> int:
        self.transfer()
        return self.out[-1]
        
    def empty(self) -> bool:
        return not self.inc and not self.out
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()