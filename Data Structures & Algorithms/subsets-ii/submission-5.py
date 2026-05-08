class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # use sort to group duplicate togather
        # Time O(n* 2^n)
        # Space O(n)
        curr = []
        res = []
        nums.sort()
        def gen(i):
            if i >= len(nums):
                res.append(curr[:])
                return

            # include
            curr.append(nums[i])
            gen(i+1)
            curr.pop()

            # exclude
            # If I choose to exclude nums[i], I also skip all later duplicates of the same value.
            while i+1 <= len(nums) - 1 and nums[i+1] == nums[i]:
                # skip duplicate
                i+=1
            gen(i+1)
        
        gen(0)
        return res
