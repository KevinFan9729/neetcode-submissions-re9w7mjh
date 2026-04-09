class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack?
        # [0,  1, 2, 3, 4, 5, 6]
        # [30,38,30,36,35,40,28]
        # [           2  1,  0, 0]
        
        # we go from right to left (future to past)
        # the result of the right most elemet is always 0
        # for each day i, skip over days that are not warmer than the temp at i
        # if you find a day that is cooler than the top
            # compute res[i] = top index - i
        # if you find a day that is warmer than the top
            # pop the stack util you can find a warmer day, the the stack is empty res[i] = 0
        # push the current day into the stack as it may be warmer than some of the days in the past
        # Time O(n)
        # Space O(n)

        temp_idx_stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)-1, -1, -1):
            while temp_idx_stack and temperatures[temp_idx_stack[-1]] <= temperatures[i]:
                # if the current temp is greater than top (future temp)
                # the top is useless thus can be discarded
                temp_idx_stack.pop()
            if len(temp_idx_stack) == 0:
                res[i] = 0
            else:
                res[i] = temp_idx_stack[-1] - i
            
            temp_idx_stack.append(i)
        return res
