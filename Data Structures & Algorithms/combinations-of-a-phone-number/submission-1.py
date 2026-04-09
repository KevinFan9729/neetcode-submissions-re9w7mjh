class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # O(3^n *n)
        if not digits:
            return []
        # first make mapping
        mapping = {}
        letters = "abcdefghijklmno"
        letter_index = 0
        for i in range(2, 7):
            if i not in mapping:
                mapping[str(i)]= []
            for _ in range(3):
                mapping[str(i)].append(letters[letter_index])
                letter_index+=1
        mapping["7"] = ["p", "q", "r", "s"]
        mapping["8"] = ["t", "u", "v"]
        mapping["9"] = ["w", "x", "y", "z"]

        res = []
        curr = []
        def comboGen(digit_index):
            if len(curr) == len(digits):
                tmp = curr.copy() #O(n)
                tmp = "".join(tmp)
                res.append(tmp)
                return
    
            if digit_index >= len(digits):
                return
            
            current_digit = digits[digit_index]
            for letter in mapping[current_digit]:
                curr.append(letter)
                comboGen(digit_index +1)
                curr.pop()

        comboGen(0)
        return res