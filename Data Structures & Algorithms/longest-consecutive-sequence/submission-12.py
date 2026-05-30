class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we do not want to do repeated work in this
        # can we solve recurisvely?
        # grow(i) starting from i want is the longest consective sequence?
        # We have n states,
        # and each n is computed once
        # Time O(n)
        # Space O(n)
        if len(nums) == 0:
            return 0
        lookup = set(nums)
        memo = {}
        def grow(num):
            maxLen = 1
            if num in memo:
                return memo[num]
            if num + 1 in lookup:
                length = 1 + grow(num+1)
                maxLen = max(maxLen, length)
            else:
                return 1
            memo[num] = maxLen
            return maxLen 
        ans = 1
        for num in lookup:
            ans = max(ans, grow(num))

        return ans