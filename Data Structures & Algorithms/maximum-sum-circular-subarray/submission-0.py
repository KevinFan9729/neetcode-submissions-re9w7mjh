class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # we can use kadane algo
        # for the middle piece is like the regular kadane
        # but at the end, we know that the subarray can loop around (this is circular afterall)
        # if we keep track of min sum of regular sub array, the max circular sum can be sum of total - min of regular
        # Time O(n)
        # Space O(1)

        currSumMax = 0
        currSumMin = 0
        localMax = nums[0]
        localMin = nums[0]
        totalSum = sum(nums)
        
        for i in range(len(nums)):
            currSumMax += nums[i]
            currSumMin += nums[i]
            localMax = max(localMax, currSumMax)
            localMin = min(localMin, currSumMin)
            currSumMax = max(currSumMax, 0) # negative sum up to i will not contribute to max, 0 is a fresh start
            currSumMin = min(currSumMin, 0)

        if localMax <0:
            return localMax # if localMax is neg, this means that the whole array is neg (otherwise we will have a positive or 0 at least)
        maxCircuar = totalSum - localMin

        return max (maxCircuar, localMax)