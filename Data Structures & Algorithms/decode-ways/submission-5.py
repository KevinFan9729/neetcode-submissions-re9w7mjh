class Solution:
    def numDecodings(self, s: str) -> int:
        # only single digit or double digts can be decoded
        # for single digit
            # single digit can be anything from 1-9, (single digit cannot be 0!)
        # for double digit
            # if the first digit is 1, the second digit can be 0-9
            # if the first digit is 2, the second digit can be 0-6
            # if the first digit is 3 or above, this case is invalid! (max is 26)
        # we will solve this recursively
            # at every step, decode one digit or 2 digits 
        # count(index) where index represents the current index to decode

        # O(n) in time there are only n unqiue states
        # O(n) in space

        memo = {}

        def count(index):
            if index >= len(s): # processed the entire string, index is at the end of the string s
                return 1 #valid path to dcode the entire string!
            if s[index] == "0": # no leading 0
                return 0 #not a valid path to decode
            if index in memo:
                return memo[index]
            
            # one digit
            oneDigit = count(index + 1)

            twoDigit = 0
            # two digits
            if (index +1 <= len(s) - 1 and ((s[index] == "1" and s[index+1] in "0123456789") or 
            (s[index]=="2" and s[index+1] in "0123456"))):
                twoDigit = count(index+2)

            totalCount = oneDigit + twoDigit
            memo[index] = totalCount
            return totalCount
        
        ans = count(0)
        return ans