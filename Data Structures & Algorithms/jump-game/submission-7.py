class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy also work here
        # can I keep extending the farthest reachable boundary before I hit an unreachable index?
        # if I can reach R, <=R are also reachable

        furtherest = 0 # global furtherest
        for i in range(len(nums)):
            if i > furtherest: # current index is beyond what is reachable
                return False
            if furtherest >= len(nums)-1: # early stop example [1,2,50,0,0,0,0,1]
                return True
            furtherest = max(furtherest, i + nums[i]) # current furtherest reachable index is current pos + max jump at i

        return True