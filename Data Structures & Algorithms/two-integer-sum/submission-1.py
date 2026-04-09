class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # val: index

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff],idx]
            hashmap[num] = idx # note this hash map only if and only if the diff is not found in the map
        