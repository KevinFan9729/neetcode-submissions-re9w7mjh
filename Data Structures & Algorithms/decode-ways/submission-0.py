class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {} # at each index, how many way can you split?
        def decode_ways(index: int) -> int:
            # O(2^n)
            # If we have processed the entire string, there is 1 valid decoding (doing nothing more)
            if index == len(s):
                return 1
            
            if index in memo:
                return memo[index]
        
            # If the current digit is '0', it can't be decoded
            if s[index] == '0':
                return 0
            
            # at each index, do we want to have one digit or two digits?
            # one digit
            count = decode_ways(index + 1) 
            
            # Decode the current and the next digit if they form a valid number (10-26)
            if index + 1 < len(s) and (s[index] == '1' or (s[index] == '2' and s[index + 1] in '0123456')): #two digits
                count += decode_ways(index + 2)
            
            memo[index] = count
            return count
        
        return decode_ways(0)