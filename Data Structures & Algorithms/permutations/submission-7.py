class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Time O(n*n!)
        # Space O(n)
        curr = []
        res = []
        seen = set()
        def gen():
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for i in range(len(nums)):
                if i in seen:
                    continue
                curr.append(nums[i])
                seen.add(i)
                gen()
                seen.remove(i)
                curr.pop()
        gen()
        return res
