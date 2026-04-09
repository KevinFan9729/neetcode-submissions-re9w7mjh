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
            if index >= len(nums): # if index == len(nums), we are out of index!
                return
            
            # include the number
            curr_combo.append(nums[index])
            comboGen(index, curr_sum = curr_sum + nums[index])
            curr_combo.pop()

            # excluding the number
            comboGen(index + 1, curr_sum)
        comboGen(0, 0)
        return res

        