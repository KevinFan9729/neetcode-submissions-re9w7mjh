class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # we have two choices at each step
        # include the current number
        # exclude the current number
        res = []
        curr_combo = []
        candidates.sort() # group duplicate together
        def comboGen(curr_index, curr_sum):
            if curr_sum == target:
                if curr_combo not in res: # prevent duplicate from being added
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

            # exclude the current number
            comboGen(curr_index +1, curr_sum)
        
        comboGen(0, 0)
        return res