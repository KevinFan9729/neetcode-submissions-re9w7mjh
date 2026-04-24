class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # at each step we need to choose number into our result
        # I notice that the start of the permutation needs to be unique
        # we should track used item with indices now
        # Time O(n!*n)
        # space O(n)
        res = []
        used = set()
        nums.sort()
        def gen(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            for i in range(len(nums)-1, -1, -1):
                if i in used:
                    continue # index was used before
                prevIdx = i -1
                currIdx = i
                if prevIdx != -1:
                    if nums[prevIdx] == nums[currIdx]:
                        if prevIdx in used:
                            continue
                curr.append(nums[i])
                used.add(i)
                gen(curr)
                curr.pop()
                used.remove(i)
            return
        gen([])
        return res