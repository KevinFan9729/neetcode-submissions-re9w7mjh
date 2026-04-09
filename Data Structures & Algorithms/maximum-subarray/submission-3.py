class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def helper(index, curr_sum):
            nonlocal max_val
            if index == len(nums):
                return curr_sum
            
            # Calculate the maximum subarray sum ending at this index
            curr_sum = max(nums[index], nums[index] + curr_sum)
            
            # Update the global maximum
            max_val = max(max_val, curr_sum)
            
            # Recurse to the next index
            return helper(index + 1, curr_sum)
        
        max_val = nums[0]
        
        # Start recursion from the first element
        helper(0, 0)
        
        return max_val
