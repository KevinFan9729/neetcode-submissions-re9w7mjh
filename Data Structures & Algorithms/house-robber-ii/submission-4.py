class Solution:
    def rob(self, nums: List[int]) -> int:
        # I am thinking robbing the first house will cause you not able to rob the last house,
        # and not robbing the first house will make you be able to rob the last house if the house before the last house is not rob, 
        # so basically we run the regular house robber algo (assume linear) but we run twice, once last house is exlcudedd (so you can rob the first if needed)
        # and once is where the first house is excluded  (so you can rob the last if needed)
        # so first rob from 0 to n-2 (exclude the last house)
        # second rob from 1 to n-1 (exclude the first house)
        # Time O(n)
        # Space O(n)
        if len(nums) == 1:
            return nums[0]
        def linearRob(i):
            if i >= len(houses):
                return 0
            if i in memo:
                return memo[i]
            # rob the current house
            robCurr = houses[i] + linearRob(i+2)
            # skip the current house
            skipCurr = linearRob(i+1)
            maxRob = max(robCurr, skipCurr)
            memo[i] = maxRob
            return maxRob
        
        houses = nums[0:len(nums)-1]
        memo = {}
        excludeLast = linearRob(0)

        houses = nums[1:]
        memo = {}
        excludeFirst = linearRob(0)
        
        return max(excludeLast, excludeFirst)