class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ArraySum = sum(nums)
        rangeSum = 0
        for i in range(1, len(nums)+1):
            rangeSum+=i
        return rangeSum - ArraySum