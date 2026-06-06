class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # without considering the both ends
        # we have a regular linear array which we can find the max sum sub array
        # if we consider both end
        # we can compute the max circular sum by using the total - middle min sum
        # Time: O(n)
        # Space: O(n)
        n = len(nums)
        memo = {}
        sys.setrecursionlimit(3000)
        def midFind(i): # max and min of subarray starting at i
            # we can extend the curr subarray or have a new start
            if i >= n: # ranout of numbers
                return (0,0) # max and min
            if i in memo:
                return memo[i]
            minVal = float('inf')
            maxVal = float('-inf')
            extendMax = nums[i] + midFind(i+1)[0]
            extendMin = nums[i] + midFind(i+1)[1]
            newStart = nums[i]

            minVal = min(minVal, extendMax, extendMin, newStart)
            maxVal = max(maxVal, extendMax, extendMin, newStart)
            memo[i] = (maxVal, minVal)
            return (maxVal, minVal)

        midMax, midMin = midFind(0)
        linearMin = float('inf')
        linearMax = float('-inf')
        for start in range(n):
            linearMax = max(midFind(start)[0], linearMax)
            linearMin = min(midFind(start)[1], linearMin)

        totalSum = sum(nums)
        if linearMax <0:
            return linearMax # if linear max is negative, this means the midMin is also negative (array is neg)
        
        circularMax = totalSum - linearMin
        return max(circularMax, linearMax)