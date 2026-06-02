class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # first we need a mapping of the digit to all the character it can represnet 
        # after we have that mapping we can do backtracking
        # i is the pointer on which char in the digit
        # each step we have 3 or 4 choices
        # say the length of the character is n
        # Time: O(n * 4^n)
        # Space: O(n) recursion/temp path, excluding output
        # Output space: O(n * 4^n)
        if len(digits) == 0:
            return []
        char_val = ord('a')-1
        dToC = {}
        for i in range(2, 7):
            for j in range(3):
                digitChar = str(i)
                if digitChar not in dToC:
                    dToC[digitChar] = []
                char_val+=1
                dToC[digitChar].append(chr(char_val))
        dToC["7"] = ["p","q", "r", "s"]
        dToC["8"] = ["t", "u", "v"]
        dToC["9"] = ["w", "x", "y", "z"]
        print(dToC)
        res = []
        tmp = []
        def backtrack(i):
            if i >= len(digits):
                res.append("".join(tmp))
                return
            for char in dToC[digits[i]]:
                tmp.append(char)
                backtrack(i+1)
                tmp.pop()
        backtrack(0)
        return res