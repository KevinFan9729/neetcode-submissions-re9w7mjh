class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # I think at each step we have two decsions?
            # include this number in to the combo
            # exclude this number from the combo
        # is this backtracking???
        # yes
        # dont need to worry about duplicate here
            # why? 
            # because we are always advancing in one decsion branch
            # we never 'look back' that cause duplicates
            # and the array has only unique values
        # the recursion depth is bounded by how many times you can add the smallest number before hitting the target
        # Time O(2^(target / min(nums))) 2 decsions needs to be made at every step
        # Space O((target / min(nums))) depth of the recursion
        res = []
        def comboGen(i, currSum, combo):
            if currSum == target:
                res.append(combo[:])
                return
            if currSum > target or i>=len(nums):
                # not valid anymore
                return
            
            # include path
            combo.append(nums[i])
            currSum+=nums[i]
            comboGen(i, currSum, combo) # dont increment i, as we can reuse number
            currSum -= combo.pop() # backtrack
            # exclude path
            comboGen(i+1, currSum, combo)

        comboGen(0,0,[])
            
        return res