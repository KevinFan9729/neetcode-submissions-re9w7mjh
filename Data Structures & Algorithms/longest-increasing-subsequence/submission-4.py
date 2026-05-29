class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # we can solve this recursively
        # define a function
        # compute(i)-> starting i what is the longest subsequence
        # Time O(n) we have n states, to compute each state we may use up n steps
        # Space O(n)
        memo = {}
        def compute(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]           
            longest = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    # we can grow this subsequence
                    length = 1 + compute(j)
                    longest = max(longest, length)
            memo[i] = longest
            return longest
        ans = 1
        for start in range(len(nums)):
            ans = max(ans, compute(start))
        return ans