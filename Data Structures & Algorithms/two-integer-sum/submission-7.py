class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # have a diff map
        # check if the complment is inside of a diff map
        # Time O(n)
        # Space O(n)
        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen:
                if i != seen[nums[i]]:
                    return [seen[nums[i]], i]
            seen[target - nums[i]] = i
        return []