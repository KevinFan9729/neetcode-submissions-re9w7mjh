class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # define a function which will return the max prod and min prod at i
        # we need to min prod as a very negative number has the possiblity to turn into a big product
        # we have n unique state
        # each unique state is computed once
        # Time O(n)
        # Space O(n)
        memo = {}
        def extreameAtI(i):
            if i == 0 :
                return nums[0], nums[0]
            if i in memo:
                return memo[i]
            maxVal = float('-inf')
            minVal = float('inf')
            # extend
            maxProd = nums[i] * extreameAtI(i-1)[0]
            minProd = nums[i] * extreameAtI(i-1)[1]
            newStart = nums[i] # new start, discard previous prodcuts
            maxVal = max(maxVal, maxProd, minProd, newStart)
            minVal = min(minVal, maxProd, minProd, newStart)
            memo[i] = (maxVal, minVal)
            return maxVal, minVal


        maxVal = float('-inf')
        for i in range(len(nums)):
            maxVal = max(maxVal, extreameAtI(i)[0])
        return maxVal
        