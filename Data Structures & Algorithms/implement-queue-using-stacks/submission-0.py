class MyQueue:
    # push into a stack normally
    # but when say you need to pop/peak from the 'queue'
    # pop from the stack1 and push to stack 2
    # depends on what you do (pop/peak) remove the last element or just return the last element
    # use stack 2 to reconstruct stack 1
    def __init__(self):
        self.normal_stack = []
        self.reverse_stack = []
        

    def push(self, x: int) -> None:
        self.normal_stack.append(x)

    def pop(self) -> int:
        if self.empty() == True:
            return None
        for i in range(len(self.normal_stack)-1):
            val_to_keep = self.normal_stack.pop()
            self.reverse_stack.append(val_to_keep)
        last_item = self.normal_stack.pop()
        # reconsurction (len-1)
        for j in range(len(self.reverse_stack)):
            val_to_keep = self.reverse_stack.pop()
            self.normal_stack.append(val_to_keep)
        return last_item
        

    def peek(self) -> int:
        if self.empty() == True:
            return None
        for i in range(len(self.normal_stack)-1):
            val_to_keep = self.normal_stack.pop()
            self.reverse_stack.append(val_to_keep)
        last_item = self.normal_stack.pop()
        self.reverse_stack.append(last_item)
        # reconsurction (len)
        for j in range(len(self.reverse_stack)):
            val_to_keep = self.reverse_stack.pop()
            self.normal_stack.append(val_to_keep)
        return last_item
        

    def empty(self) -> bool:
        if self.normal_stack == []:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()