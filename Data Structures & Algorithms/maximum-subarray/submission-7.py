class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # sliding window does not work here 
        # as we have negative values so it is not clear how to increase/decrease bounds
        # every step we can grow the subarray
        # or have a new start
        # including negative number is only worthwhile iff upto that pos, the sum is still postive
        # if up to i, the sum is negative, we need a new start

        currSum = 0
        maxSum = nums[0]

        for i in range(len(nums)):
            currSum += nums[i]
            maxSum = max(maxSum, currSum)
            currSum = max(currSum, 0) # if the running sum is negative, that portion will not contribute anymore
            
        return maxSum
