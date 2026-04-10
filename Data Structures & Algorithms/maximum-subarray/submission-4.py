class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Time O(n)
        # Space O(1)
        # at the currenSum, as long as it is postive, it has the possiblity to contributes
        # but if it negative, we will need to have a fresh start as it will negatively impact the result
        currSum = 0
        maxSum = nums[0]

        for num in nums:
            currSum = max(currSum, 0)
            currSum += num
            maxSum = max(currSum, maxSum)
        return maxSum