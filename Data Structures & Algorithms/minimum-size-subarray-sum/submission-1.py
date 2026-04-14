class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # sliding window?
        # nums[i] are all positive <- this is a key that sliding window can work
        # keep growing the window until we exceed or equal the target
        # once we are exceeding or equal the target, shrink the window in search of minium length sub array
        # we grow the window by incrementing the right pointer
        # we shrink the window bu incrementing the left pointer
        # Time O(n) even we have a nested loop, each element is visited at most once
        # Space O(1)
        left = 0
        currSum = 0
        minLen = 10**6
        for right in range(len(nums)):
            currSum += nums[right]
            while currSum >= target:
                currLen =  right-left+1
                minLen = min(minLen, currLen)
                currSum -= nums[left]
                left+=1

        return minLen if minLen != 10**6 else 0