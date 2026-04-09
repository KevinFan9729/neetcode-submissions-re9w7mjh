class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Time O(n)
        # Space O(n)
        res = nums[:]
        for num in nums:
            res.append(num)
        return res