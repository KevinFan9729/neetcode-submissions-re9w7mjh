class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # choose the next number at every step 
        # at first recursion level we will have n choices
        # second recursion level has n-1 choices
        # so on and so for
        # but we skip duplicate start
        # Time O(n* 2^n)
        # Space O(n)
        res =[]
        curr = []
        nums.sort()
        def gen(i):
            res.append(curr[:])
            for j in range(i, len(nums)):
                if j > i and nums[j-1] == nums[j]:
                    # j == i is the start of the recursion level
                    continue
                curr.append(nums[j])
                gen(j+1) # advance to the next level
                curr.pop()

        gen(0)
        return res