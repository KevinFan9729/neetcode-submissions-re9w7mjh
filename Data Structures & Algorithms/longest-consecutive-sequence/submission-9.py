class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # find the start of a sequnce
        # how
        # the start of the sequence is where num-1 does not exist
        # then count up
        # Time O(n)
        # Space O(n)
        exist = set(nums)
        longest = 0
        for num in exist:
            count = 1 # num itself is length 1
            if num -1 not in exist:# num is a start 
                while num+1 in exist: # count up
                    count += 1
                    num += 1
            longest = max(longest, count)
        return longest