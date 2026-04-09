class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n =2
        #[()()] [(())] 
        # valid means, we have matching opening and close brackets
        # also, the order or open and close brackets are important
        # natrually I am thinking of stack
        # at every step, dependings what we have on the stack
        # we can either include an open b or a close b
            # if there is no matching open b, cannot add close b
        # feels like recursion can help us?
        # gen(open_n, close_n)
        # if stack is empty, and close_n ==0, that is a valid solution
        # if stack is not empty, and close_n == 0, not valid, return
        # Time O(2^n) if not considering curr[:] and output string creation
        # Space O(n)

        stack = []
        res = []
        curr = []
        def gen(open_n, close_n):
            if len(stack) == 0 and close_n == 0:
                res.append("".join(curr[:]))
                return
            if len(stack) != 0 and close_n == 0:
                return
            if open_n < 0 or close_n <0:
                return
            
            if len(stack) == 0: # when stack is empty
                # we can only include open here
                stack.append("(")
                curr.append("(")
                gen(open_n-1, close_n)
                # backtrack/undo
                stack.pop()
                curr.pop()
            elif stack[-1] == "(":
                # we can either add a close or open here
                # include open
                stack.append("(")
                curr.append("(")
                gen(open_n-1, close_n)
                # backtrack
                stack.pop()
                curr.pop()
                # include close
                stack.pop()
                curr.append(")")
                gen(open_n, close_n-1)
                # backtrack
                stack.append("(")
                curr.pop()
        
        gen(n,n)
        return res