class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # lest use a hashmap
        # Time O(n!*n)
        # Space O(n)
        coutMap = defaultdict(int)

        for num in nums:
            coutMap[num] += 1
        res = []
        curr = []
        def gen():
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            for num in coutMap.keys():
                if coutMap[num] <= 0:
                    continue
                curr.append(num)
                coutMap[num]-=1
                gen()
                coutMap[num]+=1
                curr.pop()

        gen()
        return res