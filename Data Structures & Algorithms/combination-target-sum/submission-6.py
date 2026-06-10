class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # hmmmmm we need to return the actual combination array
        # this means we need to backtrack
        # we can define a fucntion which record the currSum as the sum of the combo
        # we can pick the same number an unlimited number of time 
        # Time: exponential in the worst case
        # Space: O(target / min(nums))
        combo = []
        res = []
        def backtrack(i, currSum):
            if currSum > target or i >= len(nums):
                return
            if currSum == target:
                res.append(combo[:])
                return

            
            # for the current i, we can include or exclude
            # include
            combo.append(nums[i])
            # the same number can be used unlimited time
            backtrack(i, currSum +nums[i])
            combo.pop()
            # exculde
            backtrack(i+1, currSum)
        
        backtrack(0, 0)
        return res


