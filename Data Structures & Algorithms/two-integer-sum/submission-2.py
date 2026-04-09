from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffmap = defaultdict(int)
        for i in range(len(nums)):
            diffmap[target - nums[i]] = i

        for i in range(len(nums)):
            index = i
            index2 = diffmap.get(nums[i])
            if index2 and index != index2:
                if index > index2:
                    return [index2, index]
                else:
                    return [index, index2]

        