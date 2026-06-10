class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we do not want to do repeated work in this
        # can we solve recurisvely?
        # grow(num) starting from num want is the longest consective sequence?
        # We have n states,
        # and each n is computed once
        # Time O(n)
        # Space O(n)
        lookup = set(nums)
        memo = {}
        def grow(num):
            maxLen = 0
            if num in memo:
                return memo[num]
            if num +1 in lookup:
                length = 1 + grow(num +1)
                maxLen = max(maxLen, length)
            else:
                # end of a chain
                memo[num] = 1
                return 1
            memo[num] = maxLen
            return maxLen
        maxLen = 0
        for num in lookup:
            maxLen = max(maxLen, grow(num))
        return maxLen