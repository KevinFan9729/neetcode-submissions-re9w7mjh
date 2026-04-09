class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # we do not need to worry about invalid input as the question stated
        # Time O(n)
        # Space O(1) if not considering the output
        ops = {"+", "C", "D"}
        res = []
        for o in operations:
            if o not in ops:
                res.append(int(o))
            else:
                if o == "+":
                    num1 = res[-1]
                    num2 = res[-2]
                    num3 = num1+num2
                    res.append(num3)
                elif o == "C":
                    res.pop()
                else:
                    ans = res[-1]*2
                    res.append(ans)
        
        return sum(res)