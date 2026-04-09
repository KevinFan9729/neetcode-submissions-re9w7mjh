class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: # the total sum is odd, you can never split nums into two even sum partition!
            return False
        target = total // 2
        memo = {}
        # each unique state (index, curr_sum) is computed only once
        # unqiue state is bounded by the index and curr_sum
        # curr_sum is in a range of 0 to target
        # O(n * target) in space and time
        def canSumToTarget(index, curr_sum):
            if curr_sum == target:
                return True
            if curr_sum > target: # stop when you exceed the target
                return False
            if index >= len(nums): # ran out of numbers
                return False
            if (index, curr_sum) in memo:
                return memo[(index, curr_sum)]
            # two choices, include current num or not
            include = canSumToTarget(index +1, curr_sum = curr_sum + nums[index])

            exclude = canSumToTarget(index +1, curr_sum)

            canReach = include or exclude

            memo[(index, curr_sum)] = canReach

            return canReach
        res = canSumToTarget(0 , 0)
        return res