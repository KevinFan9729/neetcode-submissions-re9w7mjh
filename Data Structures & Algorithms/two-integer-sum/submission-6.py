class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time O(n)
        # Space O(n)

        seen = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                if i != seen[diff]:
                    return [seen[diff], i]
            seen[nums[i]] = i
        return []