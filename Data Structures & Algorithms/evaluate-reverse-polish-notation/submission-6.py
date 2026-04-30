class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # can we use a stack?
        # when we meet a number we push to the stack
        # when we meet an operator, we pop twice and perform the operation and push res to stack
        # final result will be the top of the stack
        # order for / and - are important
        # Time O(n)
        # Space O(n)

        stack = []

        for item in tokens:
            if item not in {"+", "-", "*", "/"}:
                stack.append(int(item))
            elif item == "+":
                left = stack.pop()
                right = stack.pop()
                res = right + left
                stack.append(res)
            elif item == "-":
                left = stack.pop()
                right = stack.pop()
                res = right - left
                stack.append(res)
            elif item == "*":
                left = stack.pop()
                right = stack.pop()
                res = right * left
                stack.append(res)
            elif item == "/":
                left = stack.pop()
                right = stack.pop()
                res = int(right / left)
                stack.append(res)
        return stack[-1]