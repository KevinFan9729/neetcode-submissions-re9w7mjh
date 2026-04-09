class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def helper(index):
            nonlocal max_val
            if index == 0:
                return nums[0]  # Base case: the max subarray ending at the first element is the element itself
            
            # Recursive case
            # Either start a new subarray at this index or extend the subarray ending at index-1
            max_ending_here = max(nums[index], nums[index] + helper(index - 1))
            
            # Track the global maximum
            max_val = max(max_val, max_ending_here)
            
            return max_ending_here
        
        max_val = nums[0]
        
        # Start recursion from the last element
        val = helper(len(nums) - 1)
        max_val = max(max_val, val)
        
        return max_val