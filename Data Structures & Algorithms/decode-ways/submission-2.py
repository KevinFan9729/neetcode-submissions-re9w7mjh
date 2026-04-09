class Solution:
    def numDecodings(self, s: str) -> int:
        # at each step, we can take one character or two characters
        # if we take one character, it can be anything from 1-9
        # if we take two characters, we have serval considerations based on the first digit
            # if digit_a is 1, then digit_b can be anything from 0-9
            # if digit_a is 2, then digit_b can only be 0-6
            # if digit_a is >2, we cannot have a second digit
        memo = {}
        def decodeCount(curr_index):
            if curr_index >= len(s):
                return 1 #valid decod
           # If the current digit is '0', it can't be decoded
            if s[curr_index] == '0':
                return 0
            if curr_index in memo:
                return memo[curr_index]
            
            # one digit
            count = decodeCount(curr_index + 1)

            # two digits
            if curr_index + 1 <= len(s)-1 and (s[curr_index] == "1" or (s[curr_index] == "2" and s[curr_index+1] in "0123456")):
                count += decodeCount(curr_index + 2)
            memo[curr_index] = count
            return count
        ans = decodeCount(0)
        return ans

        