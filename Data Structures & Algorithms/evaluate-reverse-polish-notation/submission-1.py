from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # O(n)
        # use a stack
        # push numbers into the stack
        # when encounter an operator, pop two numbers out of the stack,
        # compute the value, and push the result back to the stack
        # continue till we run out of element in the tokens list
        # assuming always to have valid inputs 
        if len(tokens) == 1:
            return int(tokens[0])
        stack = deque()
        operators = set(["*", "-", "/", "+"])
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                ans = int(eval(f"{val1} {token} {val2}"))
                stack.append(ans)

        return stack.pop()