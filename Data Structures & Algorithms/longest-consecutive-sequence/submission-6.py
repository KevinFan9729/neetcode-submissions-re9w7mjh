class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # hashset? as lookup is O(1)?
        # realize the a number is the *start* if it has no previous number
        # if we find a start, we can compute the length of the sequence
        # keep updating a global longest
        # this way we truly skip the middle numbers calcuation
        # Time O(n)
        # Space O(n)

        longest = 0
        lookup = set(nums)
        for num in lookup:
            # try to find the start
            prev = num - 1
            if not (prev in lookup):
                current = num
                curr_len = 1
                next_num = current + 1
                while next_num in lookup:
                    curr_len += 1
                    next_num += 1
                longest = max(longest, curr_len)
        return longest
