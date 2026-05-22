class Solution:
    def isHappy(self, n: int) -> bool:
        # use a seen hash set to check if the result is seen or not
        # 100%10 = 0
        # 100//10 = 10 shift
        # 10%10 = 0
        # 10//10 = 1
        # 1%10 = 1
        # Time: O(number of computed states * digits per state)
        # Space O(number of unique result computed)
        seen = set()
        
        def computeSum(n):
            res = 0
            while n > 0:
                res+=(n%10)**2
                n = n // 10 # shift
            return res
        
        while True:
            n = computeSum(n)
            if n in seen:
                return False
            if n == 1:
                return True
            seen.add(n)