class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # the question is really asking
        # can we find a window of size k+1 at most (can be smaller or equal)
        # do we have any duplicate?
        # sliding window of fixed size
        # Time O(n)
        # Space O(n)
        winSize = k + 1
        wind = set()
        left = 0       
        for right in range(len(nums)):
            if right - left > k:
                wind.remove(nums[left])
                left += 1
            if nums[right] in wind:
                return True 
            wind.add(nums[right])
        return False 