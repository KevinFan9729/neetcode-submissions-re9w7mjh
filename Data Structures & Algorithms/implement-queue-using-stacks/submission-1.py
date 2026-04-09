class MyQueue:
    # push into a stack normally
    # but when say you need to pop/peak from the 'queue'
    # pop from the stack1 and push to stack 2
    # depends on what you do (pop/peak) remove the last element or just return the last element
    # use stack 2 to reconstruct stack 1
    def __init__(self):
        self.normal_stack = [] # for incoming
        self.reverse_stack = [] # for outgoing
        

    def push(self, x: int) -> None:
        self.normal_stack.append(x)

    def pop(self) -> int:
        if self.empty() == True:
            return None
        if len(self.reverse_stack) == 0:
            while self.normal_stack:
                val = self.normal_stack.pop()
                self.reverse_stack.append(val)
            val = self.reverse_stack.pop()
        else:
            val = self.reverse_stack.pop()
        return val
        

    def peek(self) -> int:
        if self.empty() == True:
            return None
        if len(self.reverse_stack) == 0:
            while self.normal_stack:
                val = self.normal_stack.pop()
                self.reverse_stack.append(val)
        else:
            val = self.reverse_stack[-1]
        return val
        

    def empty(self) -> bool:
        return not self.normal_stack and not self.reverse_stack 
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()