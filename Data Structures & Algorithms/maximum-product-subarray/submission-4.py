class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        memo = {}
        def maxProdAtI(i):
            if i == 0:
                return nums[i], nums[i]
            if i in memo:
                return memo[i]
            bestProd = nums[i] * maxProdAtI(i-1)[0]
            worstProd = nums[i] * maxProdAtI(i-1)[1]
            newStart = nums[i]

            best = max(bestProd, worstProd, newStart)
            worst = min(bestProd, worstProd, newStart)
            memo[i] = best, worst
            return best, worst

        maxProd = nums[0]
        for i in range(len(nums)):
            bestAtI , _ = maxProdAtI(i)
            maxProd = max(maxProd, bestAtI)
        return maxProd