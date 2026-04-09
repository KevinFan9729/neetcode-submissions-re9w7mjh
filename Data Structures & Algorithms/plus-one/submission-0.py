class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # need to watch out for carry
        # say if we have a carray (digit+1==10)
            # we set the current digit to 0
            # we set the carray bit to 1
        # we can consider the digits list as a stack
            # we pop the top of the stack
            # add one to the top
            # if top == 10
                # appendleft 0 to the current
                # carry = 1
            # go into a loop to add the rest of the numbers
        # O(n) in time
        # O(n) in memory due to deque
        res = deque()
        carry = 1 # initially, we want to plus 1 to the last digit
        while digits:
            lastDigit = digits.pop()
            currSum = lastDigit + carry
            if currSum == 10:
                carry = 1
                res.appendleft(0)
            else:
                carry = 0
                res.appendleft(currSum)
        if carry == 1:
            res.appendleft(1)
        return list(res)