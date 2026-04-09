class Solution:
    def isHappy(self, n: int) -> bool:
        # split all numbers
        # check if the square res is in the set
        # if so, return false, there is a cycle
        # if the res is 1, return True

        res = 0
        seen = set()

        while res != 1:
            res = 0
            # %10 to get the last digit
            # //10 to get rid of a the last digit
            while n:
                lastDigit = n%10
                res += lastDigit**2
                n=n//10
            if res in seen:
                return False
            n = res # update n
            seen.add(res)
        return True