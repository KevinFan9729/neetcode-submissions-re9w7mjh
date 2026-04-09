class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # target sum is sum(nums)/2
        # if the target sum is a float return False immediately as nums has only integers
        # then we just need to find a subarray with a sum reaching the target sum
        # O(n*target_sum) instead of O(2^n)
        totalSum = sum(nums)
        target_sum_check = totalSum % 2
        target_sum = totalSum//2
        if target_sum_check != 0:
            return False

        dp = set()
        dp.add(0)
        dp.add(nums[-1])
        for i in range(len(nums)-2, -1, -1):
            nextDP = set() # dp size cannot be changed while we are looping through it, we will have a temp set!
            for j in dp:
                tmpSum = nums[i] + j
                if tmpSum == target_sum:
                    return True
                nextDP.add(j)
                nextDP.add(tmpSum)
            dp = nextDP
        return False