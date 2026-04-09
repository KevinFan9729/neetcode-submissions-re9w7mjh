class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" == num1 or "0" == num2:
            return "0"
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = [0] * (len(num1)+ len(num2))
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1+i2] += digit
                res[i1+i2+1] += res[i1+i2] // 10 # carry
                res[i1+i2] = res[i1+i2] % 10 # actual number at res[i1+i2]
        ans = ""
        leadingZero = True
        for i in range(len(res)-1, -1, -1):
            if res[i] == 0 and leadingZero: 
                continue
            else:
                leadingZero = False
            ans += str(res[i])
        return ans