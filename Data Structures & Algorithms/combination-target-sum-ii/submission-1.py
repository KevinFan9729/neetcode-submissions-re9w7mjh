class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # we have two choices at each step
        # include the current number
        # exclude the current number
        # O(n2^n)
        res = []
        curr_combo = []
        candidates.sort() # group duplicate together
        def comboGen(curr_index, curr_sum):
            if curr_sum == target:
                res.append(curr_combo.copy())
                return
            if curr_index >= len(candidates): # run out of numbers
                return
            if curr_sum > target:
                return
            
            # include the current number
            curr_combo.append(candidates[curr_index])
            comboGen(curr_index + 1, curr_sum= curr_sum+ candidates[curr_index])
            curr_combo.remove(candidates[curr_index])

            # exclude the current number (skip duplicate number to prevent duplicate combinations)
            # in this branch we will not have the number that has occurred more than once
            while  curr_index+ 1 < len(candidates) and candidates[curr_index] == candidates[curr_index+1]:
                curr_index += 1
            comboGen(curr_index +1, curr_sum)
        
        comboGen(0, 0)
        return res