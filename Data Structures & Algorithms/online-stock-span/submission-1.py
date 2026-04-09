class StockSpanner:
    # store (price, span)
    # monotonic stack,' bottom is strictly larger
    # Time O(n)
    # Space O(n)
    def __init__(self):
        self.stocks = []

    def next(self, price: int) -> int:
        span = 1
        while self.stocks and price >= self.stocks[-1][0]:
            span+=self.stocks[-1][1]
            self.stocks.pop()
        self.stocks.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)