class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # [1,2,3,0,1] -> greedily take the max step does not work
        # track the farthest index reachable so far
        # loop through the array
        # at index i say you can reach i
        # then track what is the farthest you can reach
        # if the farthest we can reach is equal or more than len(nums)-1
        # then we can reach or at i = len(nums) -2 # second last index and farthest is not the end, return false
        # Time O(n)
        # Space O(1)
        farthest = 0
        for i in range(len(nums)-1):
            # Is index i within the farthest reachable boundary I have established so far?
            # if i is <= farthest then i is reachable
            if i <= farthest:
                farthest = max(farthest, i + nums[i])
        if farthest >= len(nums)-1:
            return True
        return False
