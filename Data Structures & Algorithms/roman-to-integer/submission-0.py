class Solution:
    def romanToInt(self, s: str) -> int:
        # need to be careful of special cases
        lookup = {"I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000}

        idx = len(s)-1
        res = 0 
        while idx >= 0:
            curr_roman = s[idx]
            # special cases:
            next_idx = idx - 1
            if curr_roman in {"V", "X"}:
                if next_idx >=0:
                    if s[next_idx] == "I":
                        res += lookup[curr_roman]
                        res -= lookup[s[next_idx]]
                        idx -= 2
                        continue
            elif curr_roman in {"L", "C"}:
                if next_idx >=0:
                    if s[next_idx] == "X":
                        res += lookup[curr_roman]
                        res -= lookup[s[next_idx]]
                        idx -= 2
                        continue
            elif curr_roman in {"D","M"}:
                if next_idx >=0:
                    if s[next_idx] == "C":
                        res += lookup[curr_roman]
                        res -= lookup[s[next_idx]]
                        idx -= 2
                        continue
            res += lookup[curr_roman]
            idx-=1
        return res 