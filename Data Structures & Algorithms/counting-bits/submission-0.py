class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        def countOnes(num):
            count = 0
            while num:
                if num & 1:
                    count+=1
                num = num>>1
            return count
        for i in range(n+1):
            res.append(countOnes(i))
        return res