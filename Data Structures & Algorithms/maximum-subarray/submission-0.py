class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum= nums[0]
        curr_sum = 0
        for index in range(len(nums)):
            if curr_sum <= 0:
                curr_sum = 0 # reset curr_sum, discard previous sub array sum
            curr_sum += nums[index]
            max_sum = max(max_sum, curr_sum)
        
        return max_sum