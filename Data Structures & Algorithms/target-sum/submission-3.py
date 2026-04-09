class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # we can solve this recursively
        # at each step we can +the current number or - the current number
        # count(index, currSum)
        # base case:
            # if index >= len(nums) and currSum != target, not a valid path
            # if index >= len(nums) and currSum == target, a valid path
        # O(2^n) in time as we have 2 decisions at every step
        # O(n) in space
        
        def count(index, currSum):
            if index >= len(nums) and currSum != target:
                return 0
            if index >= len(nums) and currSum == target:
                return 1
            
            plus = count(index+1, currSum+nums[index])
            minus = count(index+1, currSum-nums[index])
            total = plus + minus
            return total
        ans = count(0,0)
        return ans