class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # we can use kadane algo (dp version)
        # for the middle piece is like the regular kadane
        # but at the end, we know that the subarray can loop around (this is circular afterall)
        # if we keep track of min sum of regular sub array, the max circular sum can be sum of total - min of regular
        # Time O(n)
        # Space O(n)

        totalSum = sum(nums)
        memo1= {}
        def MaxATi(i):
            if i == 0:
                return nums[0]
            if i in memo1:
                return memo1[i]
            extend = nums[i] + MaxATi(i-1)
            newStart = nums[i]
            best = max(extend, newStart)
            memo1[i] = best
            return best
        memo2={}
        def MinAti(i):
            if i == 0:
                return nums[0]
            if i in memo2:
                return memo2[i]
            extend = nums[i] + MinAti(i-1)
            newStart = nums[i]
            worst = min(extend, newStart)
            memo2[i] = worst
            return worst
        
        localMax = nums[0]
        localMin = nums[0]
        for i in range(len(nums)):
            localMax = max(localMax, MaxATi(i))
            localMin = min(localMin, MinAti(i))
        
        if localMax < 0:
            return localMax
        
        maxCircuar = totalSum - localMin

        return max (maxCircuar, localMax)

        
        