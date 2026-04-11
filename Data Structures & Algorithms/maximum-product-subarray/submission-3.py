class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # at every step we have three choices
        # we do 
            # multiply this number with the max product at i-1
            # multiply this number with the min product at i-1
            # just keep the current number
        # why are we doing this?
            # becuase the sign of nums[i] is important
            # if nums[i] is positive, it multiply with big positive prev will give you a good proudct
            # if nums[i] is negative, it multiply with big negative prev will give you a good proudct 
        # productHere(i) -> return (max_product_ending_at_i, min_product_ending_at_i) 
        # Time O(n) at most all memo state are computed once
        # Space O(n)
        memo = {}
        def productHere(i): # -> return (max_product_ending_at_i, min_product_ending_at_i) 
            if i < 0:
                return 1,1
            if i in memo:
                return memo[i]
            maxProd = nums[i] * productHere(i-1)[0]
            minProd = nums[i] * productHere(i-1)[1]
            curr = nums[i]
            actual_max = max(maxProd,minProd,curr)
            actual_min = min(maxProd,minProd,curr)
            memo[i] = (actual_max, actual_min)
            return memo[i]

        max_prod = nums[0]
        for i in range(len(nums)):
            bestHere, worstHere = productHere(i)
            max_prod = max(max_prod, bestHere)
        return max_prod