class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # two choices, include the current index or exclude the the index
        # index can be 0 to n-1 
        # prev_index can be -1 to n-2
        # O(n^2)
        memo = {}
        def LIS(index: int, prev_index: int) -> int:
            if index >= len(nums):
                return 0
            if (index, prev_index) in memo:
                return memo[(index, prev_index)]
            
            exclude = LIS(index+1, prev_index)

            include = 0
            if prev_index == -1 or nums[index] > nums[prev_index]:
                include = 1 + LIS(index + 1, index)
            
            ans = max(exclude, include)
            memo[(index, prev_index)] = ans

            return ans
        maxLen = LIS(0,-1)
        return maxLen