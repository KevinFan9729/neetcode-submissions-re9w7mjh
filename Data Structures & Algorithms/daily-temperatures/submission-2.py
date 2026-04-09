class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack?
        # [0,  1, 2, 3, 4, 5, 6]
        # [30,38,30,36,35,40,28]
        # [           2  1,  0, 0]
        # stack keep the index of temperatures array
        # we go from right to left (future to past)
        # the result of the right most elemet is always 0
        # for each day i, check the top (future) is cooler or warmer
            # While there are future days on the stack that are not warmer than day i (their temp ≤ current temp),
                # those future days temp are cooler than the current 
                # bad =(
                # remove them (they’re useless).
            # After this cleanup:
            # If the stack is not empty, the top is the nearest future day that is warmer →
                # res[i] = top_index - i.
            # If the stack is empty, there is no future warmer day →
                # res[i] = 0.

            # Push i onto the stack.
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
