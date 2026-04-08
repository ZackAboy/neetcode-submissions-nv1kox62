class StockSpanner:

    def __init__(self):
        self.stack = list()

    def next(self, price: int) -> int:
        self.stack.append(price)
        i = 1
        for x in self.stack:
            if self.stack[-i] <= price:
                i+=1
            else:
                break
        return i-1

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)