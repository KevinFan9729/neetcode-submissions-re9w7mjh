class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # python dict are ordered.
        # key value of the original list, value: target- list value
        diff_ls = []
        for i in nums:
            diff_ls.append(target - i)
        print(diff_ls)
        
        index = 0
        for diff in diff_ls:
            if diff in nums:
                diff_index = nums.index(diff)
                if diff_index != index:
                    break
            index += 1
        if index > diff_index:
            return [diff_index, index]
        else:
            return [index, diff_index]
            

        