class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #O(nlogn)
        max_len = 0
        sequence = 1
       
        nums = list(set(nums)) # python set is unordered! 
        nums = sorted(nums)
        if not nums:
            return 0
        for i in range(len(nums)-1):
            curr_indx = i
            next_indx = i+1
            if sequence > max_len:
                max_len = sequence
            if nums[next_indx] - nums[curr_indx] == 1:
                sequence += 1
            else:
                sequence = 1
        if sequence > max_len:
            max_len = sequence
        return max_len