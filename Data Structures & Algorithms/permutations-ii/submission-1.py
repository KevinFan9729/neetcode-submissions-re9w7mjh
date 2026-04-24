class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # at each step we need to choose number into our result
        # I notice that the start of the permutation needs to be unique
        # we can use a hash map to track unqiue start
        # Time O(n!*n)
        # space O(n)
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        res = []
        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for num in count.keys():
                if count[num] >0: # this means this num is is available
                    curr.append(num)
                    count[num] -= 1
                    dfs(curr)
                    count[num] += 1
                    curr.pop()
            
        dfs([])
        return res