class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # backtracking and we do not allow duplicate to be recursion start
        # Time O(n!*n)
        # Space O(n) # excluding output
        countMap = {}
        for num in nums:
            if num not in countMap:
                countMap[num] = 0
            countMap[num] += 1

        curr= []
        res = []
        def gen():
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for num in countMap.keys():
                if countMap.get(num, -1) > 0:
                    curr.append(num)
                    countMap[num] -= 1
                    gen()
                    curr.pop()
                    countMap[num] += 1

        gen()
        return res