class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # time O(n*n!)
        # space O(n)
        res = []
        seen = set()
        def gen(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            if len(curr) > len(nums):
                return # invalid
            for item in nums:
                if item in seen:
                    continue # do not repeatly pick the same number
                curr.append(item)
                seen.add(item)
                gen(curr)
                curr.pop()
                seen.remove(item)
            return
        gen([])
        return res