class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # we do not waht duplicates to start their new branches
        # say we have [1a, 1b, 1c, 2]
        # 1a ✅
        # 1b ❌ because 1a is not used
        # 1c ❌ because 1b is not used
        # 2  ✅
        # only 1a and 2 can be start branches
        # Time O(n!*n)
        # space O(n)

        nums.sort()
        curr = []
        res = []
        used = set()
        def gen():
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            for i in range(len(nums)):
                if i in used:
                    continue
                # previous is is equal to current
                if i > 0 and nums[i-1] == nums[i]:
                    # make sure the left most duplicate can start a branch
                    if i-1 not in used:
                        continue
                curr.append(nums[i])
                used.add(i)
                gen()
                curr.pop()
                used.remove(i)
        
        gen()
        return res