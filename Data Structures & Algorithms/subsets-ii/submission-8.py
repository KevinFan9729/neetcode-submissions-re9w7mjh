class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #[1 1 2] 
        # we will produce 1 2 and 1 2 (duplicate sets)
        # include first 1, and 2
        # include second 1 and 2
        # so when we decide to exlcude 1, we must exlcude all ones as those ones starting to include other numbers will casue duplicates

        nums.sort()
        curr = []
        res = []
        def gen(i):
            if i >=len(nums):
                res.append(curr[:])
                return
            curr.append(nums[i])
            gen(i+1)
            curr.pop()

            while i+1 <= len(nums)-1 and nums[i] == nums[i+1]:
                i+=1 # skip duplicate
            gen(i+1)
        gen(0)
        return res