class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        index_a = len(a)-1
        index_b = len(b)-1
        carry = 0
        # Time O(n)
        # Space O(n) due to output res
        while index_a >=0 or index_b >=0 or carry:
            a_num = int(a[index_a]) if index_a >= 0 else 0
            b_num = int(b[index_b]) if index_b >= 0 else 0
            res_num = a_num + b_num + carry
            res.append(str(res_num%2))
            carry = res_num//2
            index_a-=1
            index_b-=1
        
        return "".join(res[::-1])