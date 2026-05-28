class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # at every number decide if the number should goes to part 1 or part 2
        # we shoudl keep track of the sum for 1 and sum for 2
        # we can try to solve this recursively?
        # def form(sum1, i) sum2 can be expressed as sumTotal-sum1
        # we can claim victory when say we run out of number and sum1 and sum2 are equal
        # Time O(n*s) n possible indices × S possible subset sums
        # Space O(n*s)
        memo = {}
        sumTotal = sum(nums)
        if sumTotal % 2 == 1:
            # if total sum is odd, then we cannot split into 2 equal partition
            return False
        def form(sum1, i):
            if sum1 > sumTotal // 2:
                return False
            if i >= len(nums) and sum1==sumTotal-sum1:
                return True
            if i >= len(nums) and sum1 != sumTotal-sum1:
                return False
            if (sum1, i) in memo:
                return memo[(sum1, i)]
            
            addTo1 = form(sum1+nums[i], i+1)
            addTo2 = form(sum1, i+1)

            if addTo1 or addTo2:
                memo[(sum1, i)] = True
                return True
            memo[(sum1, i)] = False
            return False

        res = form(0,0)
        return res