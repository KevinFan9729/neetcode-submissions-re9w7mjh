class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic decreasing stack
        # the stack stores indices of future warmer-candidate days,
        # Time O(n)
        # Space O(n)
        stack = []
        n = len(temperatures)
        res = [0] * n

        for i in range(n-1, -1, -1):

            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop() # maintain that our stack is decreasing
            

            # stack[-1] is the index of the nearest warmer future day
            # i is today
            # future day index - today index = number of days to wait
            if not stack:
                res[i] = 0
            else:
                res[i] = stack[-1] - i
            stack.append(i)
        
        return res