class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # ok for each number we can either add or subtract
        # so two choices for each number
        # define a function which can return the number of ways to reach target sum
        # Time O(n*sum(nums))
        # Space O(n*sum(nums))
        memo = {}
        def find(i, currSum):
            if i>= len(nums) and currSum == target:
                # this is a valid path
                return 1
            elif i>= len(nums) and currSum != target:
                # not valid
                return 0

            if (i, currSum) in memo:
                return memo[(i, currSum)]
            add = find(i+1, currSum+nums[i])
            sub = find(i+1, currSum-nums[i])
            total = add + sub
            memo[(i, currSum)] = total
            return total
        
        res = find(0,0)
        return res