class Solution:
    def integerBreak(self, n: int) -> int:
        # search range is 2 to n
        # say if you break n so that the first piece is i,
        # the rest of the piece(s) are n-i
        # then we need to decide if breaking n-i further is better 
            # if the rest is NOT broken further
            # the product is i * (n-i)

            # if the rest IS borken further
            # the product is then i * breaking n-i section

        # recursive 
        # breakInt(total) where total is what what we are breaking

        # Time O(n^2)
        # Space O(n)
        
        memo = {}
        def breakInt(total):
            if total <= 2:
                return 1
            maxProd = 1
            if total in memo:
                return memo[total]
            for i in range(2, total):
                firstPiece = i 
                # not break further 
                prod1 = firstPiece * (total - firstPiece)

                # break further
                prod2 = firstPiece * breakInt(total - firstPiece)
                maxProd = max(maxProd, prod1, prod2)
            memo[total] = maxProd
            return maxProd

        res = breakInt(n)
        return res