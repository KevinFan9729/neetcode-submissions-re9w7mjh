class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum %2 !=0:
            return False
        target = totalSum//2
        dp = [False] * (target+1) #  each index i represents whether a subset sum of i is achievable with the elements seen so far
        dp[0] = True # target of 0 should always to achieveable
        
        for num in nums:
            for j in range(target, num-1, -1):
                # If dp[j - num] is True, it means there's a subset of the previous numbers that sums to j - num
                if dp[j-num]:
                    # j - num + num = j
                    dp[j] = True
                if dp[target]: # early return
                    return True
        return dp[target]