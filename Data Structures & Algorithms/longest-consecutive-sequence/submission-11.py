class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we cannot do repeated scans
        # to do O(n) time
        # we also have duplicates in this input
        # use a set to dedup and for fast lookup
        # always start at a start of a sequence
        # what is a start of a sequence?
        # if num -1 does not exists
        # Time O(n)
        # Space O(n)
        lookup = set(nums)
        longest = 0
        for num in lookup:
            if num - 1 in  lookup:
                # num is NOT a start at this point
                continue 
            length = 1
            while num +1 in lookup:
                length +=1
                num = num +1
            longest = max(longest, length)
        return longest