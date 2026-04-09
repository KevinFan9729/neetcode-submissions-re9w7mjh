class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # solve recursively?
        # count(index, currSum)
        # base case, currSum == target and we used all numbers, valid path
        # base case, index >= len(nums) but currSum!=target, we run out of number, invalid
        # at each step, we can subtract or add the number at the index 

        # O(n*m) (index, currSum) unique states are computed nonrepeatedly, index is bounded by n (len(nums)), currSum is bounded by m (target)
        # O(n*m) in space, the hash map needs to record all our states

        memo = {}
        def count(index, currSum):
            if currSum == target and index == len(nums):
                return 1
            if index >= len(nums):
                return 0
            if (index, currSum) in memo:
                return memo[(index, currSum)]
            finalCount = count(index +1, currSum = currSum+nums[index]) + count(index +1, currSum = currSum-nums[index])
            memo[(index, currSum)]= finalCount
            return finalCount
        ans = count(0,0)
        return ans
        