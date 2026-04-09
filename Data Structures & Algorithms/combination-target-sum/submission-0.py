class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # at each step, we have two choices
         # 1. select the current number
         # 2. not select the current number

        res = []
        curr_combo =[]
        memo = {}
        def comboGen(curr_index, curr_sum):
            if curr_index >= len(nums): # run out of number to choose
                return
            if curr_sum > target: # we are overshotting
                return 
            if curr_sum == target:
                res.append(curr_combo.copy())
                return
            # 1. select the current number
            curr_combo.append(nums[curr_index])
            curr_sum += nums[curr_index]
            comboGen(curr_index, curr_sum)
            curr_combo.pop()
            curr_sum -= nums[curr_index]

            # 2. not select the current number
            comboGen(curr_index+1, curr_sum)
        comboGen(0,0)
        return res