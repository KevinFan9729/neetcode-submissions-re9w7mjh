class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # a subarry means it has to be contigous
        # the array is strictly positive means we can only make progress
        # when increasing the subarray length
        # sliding window
        # we increase the window until we can get a sum larger or equal to target
        # if we hit that size, good, we record that length and we start to shrink the window
        # shrink the window until we have to grow again
        # keep recording the min length of subarrays that satisfy the condition
        # Time O(n)
        # Space O(1)
        if len(nums) == 0:
            return 0
        left, right = 0, 0
        min_len = float('inf')
        win_sum = nums[0]
        while left <= right and right < len(nums):
            if win_sum < target:
                # grow the window:
                right+=1
                if right < len(nums):
                    win_sum += nums[right]
            else:
                length = right - left +1
                min_len = min(min_len, length)
                win_sum-=nums[left]
                # shrink the window
                left +=1
        if min_len == float('inf'):
            return 0
        return min_len
