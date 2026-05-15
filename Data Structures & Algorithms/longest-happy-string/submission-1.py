class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # hmmmm can we do things greedily?
        # everytime we will choose the most available character 
        # why does this make sense
        # this kinda make sense in the way that having consecutive repeating characters is dangerous
        # and the most available character are more likely to form consecutive repeating characters
        # on other hand, less available character are more 'valuable' in this case as they can be used to break the seqeunce
        
        # Pick the character with the highest remaining count.
        # If appending it does not create three in a row, use it.
        # If it would create three in a row, pick the next highest remaining character.
        # If no other character is available, stop.
        # Time O(n)
        # Space O(n)

        choices = {"a":a, "b":b, "c":c}
        def findMaxKey(choices):
            maxVal= 0
            maxKey = ""
            for key, val in choices.items():
                if val >= maxVal:
                    maxVal = val
                    maxKey = key
            return maxKey

        res = []
        while True:
            possibleChar = findMaxKey(choices)
            if choices[possibleChar] == 0:
                break
            if len(res) >= 2 and res[-1] == res[-2] == possibleChar:
                maskedMap = choices.copy()
                del maskedMap[possibleChar]
                possibleChar = findMaxKey(maskedMap)
                if choices[possibleChar] == 0:
                    break
                res.append(possibleChar)
                choices[possibleChar] -=1
            else:
                res.append(possibleChar)
                choices[possibleChar] -=1

        return "".join(res)
            