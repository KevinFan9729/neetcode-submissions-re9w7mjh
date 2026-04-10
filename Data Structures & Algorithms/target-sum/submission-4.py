class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # for each number
        # we have two choices
        # add the number
        # subtract the number
        # recursion
        # gen(i,curr) -> return number of valid paths
        # Time O(n^2)
        # Space O(n^2)
        memo = {}
        def gen(i, curr):
            if i >= len(nums):
                if curr == target:
                    return 1
                return 0
            if (i, curr) in memo:
                return memo[(i,curr)]
            pos = gen(i+1, curr+nums[i])
            neg = gen(i+1, curr-nums[i])
            
            path = pos + neg
            memo[(i, curr)] = path
            return path
        
        res = gen(0,0)
        return res
