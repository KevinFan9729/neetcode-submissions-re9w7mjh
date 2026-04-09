class Solution:
    def isHappy(self, n: int) -> bool:
        # split all numbers
        # check if the square res is in the set
        # if so, return false, there is a cycle
        # if the res is 1, return True

        res = 0
        seen = set()

        def splitNum(n):
            # %10 to get the last digit
            # //10 to get rid of a the last digit
            out = []
            while n:
                lastDigit = n%10
                out.append(lastDigit)
                n=n//10
            return out

        while res != 1:
            res = 0
            # digits = [int(i) for i in str(n)]
            digits = splitNum(n)
            for digit in digits:
                res += digit**2
            if res in seen:
                return False
            n = res # update n
            seen.add(res)
        return True