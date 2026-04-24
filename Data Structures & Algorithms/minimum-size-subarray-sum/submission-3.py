class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # they are all postive so we can use sliding window
        # we keep expanding the window until sum is larger or eqaul to target
        # then we shrink in hope of finding a shorter winodw
        # Time O(n)
        # Space O(1)
        minLen = float('inf')
        left = 0
        currSum = 0
        for right in range(len(nums)):
            currSum += nums[right]
            while currSum >= target:
                minLen = min(minLen, right-left+1)
                currSum -= nums[left]
                left += 1

        return minLen if minLen != float('inf') else 0
