from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we can have a hashmap where we have diff as the key and value as the index
        # we then can loop the array to see if the current value is equal to diff, if we see one, then we just look up the index (map value)
        # time O(n) as we loop through the array
        # space O(n) as we have a diff hashmap
        diff_map = defaultdict(int)
        for i, val in enumerate(nums):
            diff = target - val
            diff_map[diff] = i
        res = []
        for i in range(len(nums)):
            # check if the current value is in the diff_map
            # also need to make sure we are not looking at the same index
            if nums[i] in diff_map and i !=diff_map[nums[i]]:
                res = [i, diff_map[nums[i]]]
                break# we have found the result, early break
        return res
        