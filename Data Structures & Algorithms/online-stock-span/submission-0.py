class StockSpanner:
    # use two stacks?
    # Time O(n^2)
    # Space O(n)

    def __init__(self):
        self.stocks = []
        self.temp = []

    def next(self, price: int) -> int:
        self.stocks.append(price)
        span = 1
        curr = self.stocks.pop()
        self.temp.append(curr)
        for _ in range(len(self.stocks)):
            if curr >= self.stocks[-1]:
                span+=1
                price = self.stocks.pop()
                self.temp.append(price)
            else:
                break
        while self.temp: # reconstruct the stack
            self.stocks.append(self.temp.pop())
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)