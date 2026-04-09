class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr_combo = []
        def comboGen(index, curr_sum):
            if curr_sum > target:
                return
            if curr_sum == target:
                res.append(curr_combo.copy())
                return
            # if index >= len(nums): # if index == len(nums), we are out of index!
            #     return
            for i in range(index, len(nums)): # all possible starting point
                curr_combo.append(nums[i])
                comboGen(i, curr_sum + nums[i])
                curr_combo.pop()
        comboGen(0, 0)
        return res

        