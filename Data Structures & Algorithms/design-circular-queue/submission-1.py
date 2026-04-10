class ListNode:

    def __init__(self, val, nxt, prev):
        self.val, self.next, self.prev = val, nxt, prev

class MyCircularQueue:
    # 1, 2, 3

    def __init__(self, k: int):
        # feel like we can just implement this with a list?
        self.head = ListNode(0, None, None)
        self.tail = ListNode(0, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.curr = self.head
        self.size = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        currNode = ListNode(value, self.tail, self.curr)
        self.curr.next = currNode
        self.tail.prev = currNode
        self.curr = currNode
        self.size +=1
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.size == 1:
            self.curr = self.head
        # head.next is the front
        front = self.head.next
        self.head.next = front.next
        front.next.prev = self.head
        del front
        self.size -=1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0
        
    def isFull(self) -> bool:
        return self.size == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()