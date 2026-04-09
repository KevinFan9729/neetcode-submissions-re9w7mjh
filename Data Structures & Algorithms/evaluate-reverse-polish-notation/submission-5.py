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
    # NOTE!!!!
    # // is FLOOR division
    # e.g. 5//-2 =-2.5 =-3  and  5//2 =2.5=2
    # The floor division operator // then "floors" this result. The floor of a number is the greatest integer less than or equal to that number.
    # For positive numbers, this simply truncates the decimal part (e.g., the floor of 2.5 is 2). it works BUT....
    # For negative numbers, the result is the integer further away from zero. The integers around -2.5 are -2 and -3.
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
                right_operand = compute_stack.pop() # right operand
                left_operand = compute_stack.pop() # left operand
                if operand == "+":
                    compute_stack.append(left_operand+right_operand)
                elif operand == "-":
                    compute_stack.append(left_operand-right_operand)
                elif operand == "*":
                    compute_stack.append(left_operand*right_operand)
                else: # assume "/"
                    compute_stack.append(int(left_operand/right_operand))
        ans = compute_stack[-1] # answer is the top of the stack
        return ans