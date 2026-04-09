class MinStack:

    def __init__(self):
        self.stack = []
        self.min_ls = [] # track all miniumn
        self.min_val = float('inf')
        

    def push(self, val: int) -> None:
        if val <= self.min_val:
            self.min_val = val
            self.min_ls.append(self.min_val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack[-1]
            del self.stack[-1]
            if self.min_ls:
                if val == self.min_ls[-1]:
                    del self.min_ls[-1]
                if not self.min_ls: # the min_ls is empty we need to reset the min reference
                    self.min_val = float('inf')
            else:
                self.min_val = float('inf')
        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        if self.min_ls:
            return self.min_ls[-1]
        return None
        