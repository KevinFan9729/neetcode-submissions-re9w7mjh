class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # array is all positive that is good
        # we can use slide winding for contiguous subarray then
        # expand the window until it satisfies the target, then shrink it as much as possible while still checking valid lengths.
        # if say the subarray satsify the the target then try to shrink
        # Time O(n)
        # Space O(1)
        left = 0
        currSum = 0
        minLen = float('inf')
        for right in range(len(nums)):
            currSum+=nums[right]
            while currSum >= target:
                length = right - left +1
                minLen = min(minLen, length)
                currSum -= nums[left]
                left +=1
        return minLen if minLen != float('inf') else 0