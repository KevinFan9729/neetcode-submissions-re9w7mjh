class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # get a diff array?
        # say in eg 1, we have [3,4,5,6] target 7
        # diff [4, 3, 2, 1] -> store this in a map
        # check the original compared to diff
        # Time O(n)
        # Space O(n)

        diff_map = defaultdict(int)

        for i in range(len(nums)):
            diff = target - nums[i]
            diff_map[diff] = i

        for i in range(len(nums)):
            if nums[i] in diff_map:
                if i != diff_map[nums[i]]:
                    return [i, diff_map[nums[i]]]
        return []