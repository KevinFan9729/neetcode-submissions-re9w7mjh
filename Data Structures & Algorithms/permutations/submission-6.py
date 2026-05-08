class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        curr = []
        used = set()
        def gen():
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            for i in range(len(nums)):
                if i in used:
                    continue # cannot reuse the same number
                curr.append(nums[i])
                used.add(i)
                gen()
                curr.pop()
                used.remove(i)
        gen()
        return res
