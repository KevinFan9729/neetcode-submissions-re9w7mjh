class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # insert the current number at all possible position 
        # [3]
        # [2,3] [3,2]
        # [1,2,3] [2,1,3] [2,3,1] [1,3,2] [3,1,2] [3,2,1]
        # O(n^2 * n!)
        def permuteGen(index):
            if index == len(nums):
                return [[]]
            res = []
            pers = permuteGen(index + 1)

            for p in pers:
                for insert_pos in range(len(p) +1):
                    tmp = p.copy() #O(n)
                    tmp.insert(insert_pos, nums[index]) #O(n)
                    res.append(tmp)
            return res
        return permuteGen(0)