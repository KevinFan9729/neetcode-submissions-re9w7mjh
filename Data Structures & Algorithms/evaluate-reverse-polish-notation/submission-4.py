class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # use a stack
        # assume all expressions are valid
        # where we push numbers to the stack
        # pop twice when we encounter a operator and
        # compute the result and push back to stack
        # must be careful for - and / as those operations order matter
        # stock pop will remove the top, as we pop twice, the num1 is the freshest element, num2 will be the older one(the running result)
        # so order will need to be num2-num1 or num2//num1
        # also we need to be careful of negative number
        # truncate toward zero JUST MEAN YOU GET RID OF THE DECIMAL PART LIKE 5/2=2.5 but you give 2
        # Time O(n)
        # Space O(n)
        def is_integer(s):
            try:
                int(s)
                return True
            except ValueError:
                return False

        compute_stack = []

        for operand in tokens:
            if is_integer(operand):
                compute_stack.append(int(operand))
            else:
                num1 = compute_stack.pop()
                num2 = compute_stack.pop()
                if operand == "+":
                    res = num1+num2
                    compute_stack.append(res)
                elif operand == "-":
                    res = num2-num1
                    compute_stack.append(res)
                elif operand == "*":
                    res = num1*num2
                    compute_stack.append(res)
                else: # assume "/"
                    res = int(num2/num1)
                    compute_stack.append(res)
        ans = compute_stack[-1] # answer is the top of the stack
        return ans