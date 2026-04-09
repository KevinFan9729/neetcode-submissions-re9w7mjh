class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        print(nums)
        for num in nums:
            if (num - 1) not in nums: # num - 1 is not in the set means it is a new beginning
                length = 1
                while (length + num) in nums:
                    length += 1 
                longest = max(length, longest)
        return longest
           
        