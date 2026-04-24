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
            for i in range(len(nums)):
                if i in used:
                    continue # index was used before
                nextIdx = i +1
                currIdx = i
                if nextIdx <= len(nums)-1:
                    if nums[nextIdx] == nums[currIdx]:
                        if nextIdx not in used:
                            continue
                curr.append(nums[i])
                used.add(i)
                gen(curr)
                curr.pop()
                used.remove(i)
            return
        gen([])
        return res