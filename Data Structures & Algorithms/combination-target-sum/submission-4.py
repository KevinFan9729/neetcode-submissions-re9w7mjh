class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # at each step 2 decsions
        # include this number or not
        # and for the 
        # all numbers are distinct
        # we will not have duplicate as our input is unique and dfs is one directional
        # Time O(2^n)
        # Space O(n) depth of the recursion tree, if not counting output
        res =[]

        def dfs(i, curr, curr_sum):
            if curr_sum == target:
                res.append(curr[:])
                return
            if curr_sum > target or i >= len(nums):
                # not valid
                return
            curr.append(nums[i])
            curr_sum+=nums[i]
            dfs(i, curr, curr_sum) # we may resuse the same num, so we dont increment the index
            pop_num = curr.pop() # backtrack
            curr_sum-=pop_num
            dfs(i+1, curr, curr_sum)
        dfs(0,[], 0)
        return res
            
