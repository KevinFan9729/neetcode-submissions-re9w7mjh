class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": # leading 0, no valid way to split
            return 0
        dp = [0] * (len(s) + 1)
        if s[-1] != "0": # if the last digit is zero, at index len(s)-1, there is 0 way to split
            dp[-2] = 1
        else:
            dp[-2] = 0
        dp[-1] = 1
        for i in range(len(s)-2, -1, -1):
            curr_digit = s[i]
            if curr_digit == "0": # zero in the middle, but at index i, this 0 can be considered as a leading 0 
                dp[i] = 0
            elif curr_digit == "1":
                dp[i] = dp[i+1] + dp[i+2]
            elif curr_digit == "2":
                next_digit = s[i+1]
                if next_digit in "0123456":
                    dp[i] = dp[i+1] + dp[i+2]
                else:
                    dp[i] = dp[i+1]
            else:
                dp[i] = dp[i+1]

        return dp[0]