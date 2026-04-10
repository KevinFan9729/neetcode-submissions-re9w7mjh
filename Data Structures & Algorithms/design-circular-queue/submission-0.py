class MyCircularQueue:
    # 1, 2, 3
    def __init__(self, k: int):
        # feel like we can just implement this with a list?
        self.queue = []
        self.size = k

    def enQueue(self, value: int) -> bool:
        if len(self.queue) < self.size:
             self.queue.append(value)
             return True
        return False

    def deQueue(self) -> bool:
        # expensive shifting things
        if self.queue:
            del self.queue[0]
            return True
        return False

    def Front(self) -> int:
        if self.queue:
            return self.queue[0]
        return -1

    def Rear(self) -> int:
        if self.queue:
            return self.queue[-1]
        return -1
        

    def isEmpty(self) -> bool:
        return len(self.queue) == 0
        
    def isFull(self) -> bool:
        return len(self.queue) == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()