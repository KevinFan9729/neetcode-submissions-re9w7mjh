class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # builds subsets by choosing the next element to add
        # say we have [1,2,3]
        # []
        # at this point we have 2 choices 2 and 3
        # [1]-> [1,2] ->[1,2,3]
        # [1] -> [1,3]
        
        # Time O(n * 2^n)
        # Space O(n)
        curr = []
        res = []

        def gen(i):
            res.append(curr[:])

            for j in range(i, len(nums)): # i and onward
                curr.append(nums[j])
                gen(j+1)
                curr.pop()
        gen(0)
        return res