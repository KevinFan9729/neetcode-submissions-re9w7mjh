class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # target sum is sum(nums)/2
        # if the target sum is a float return False immediately as nums has only integers
        # then we just need to find a subarray with a sum reaching the target sum
        totalSum = sum(nums)
        target_sum_check = totalSum % 2
        target_sum = totalSum/2
        if target_sum_check != 0:
            return False
        def canReachTargtSum(curr_index, curr_sum):
            if curr_index >= len(nums):
                return False # run out of number
            if curr_sum == target_sum:
                return True
            # two choices, include the current number or not
            # include the current number
            include = canReachTargtSum(curr_index+1, curr_sum = curr_sum + nums[curr_index])
            # NOT include the current number
            exclude = canReachTargtSum(curr_index+1, curr_sum = curr_sum)

            canReach = (include or exclude)
            return canReach
        
        ans = canReachTargtSum(0,0)
        return ans