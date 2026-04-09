class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # solve recursively?
        # count(index, currSum)
        # base case, index >= len(nums), we run out of number, invalid
        # currSum == target and we used all numbers, valid path
        # at each step, we can subtract or add the number at the index 

        # becuase we have 2 choices at each step, the time complexity is going to be exponential
        # O(2^n) in time where n is the size of the nums
        # O(n) in space, the call stack can go as deep as the entire nums array

        def count(index, currSum):
            if currSum == target and index == len(nums):
                return 1
            if index >= len(nums):
                return 0
            finalCount = 0 
            finalCount += count(index +1, currSum = currSum+nums[index]) + count(index +1, currSum = currSum-nums[index])
            return finalCount
        ans = count(0,0)
        return ans
        