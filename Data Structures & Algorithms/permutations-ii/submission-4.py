class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # backtracking and we do not allow duplicate to be recursion start

        curr= []
        res = []
        seen =set()
        nums.sort()# we can group duplicate togather
        def gen(i):
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for j in range(len(nums)): # we can try to pick all numbers for permutations
                if j > 0 and nums[j-1] == nums[j] and j - 1 not in seen:
                    # at the same recursion level we do not want to start at the duplicate
                    # if j-1 is in seen, that means it is used, we can pick the duplicate
                    continue
                if j in seen:
                    # item used
                    continue
                curr.append(nums[j])
                seen.add(j)
                gen(j)
                curr.pop()
                seen.remove(j)
        gen(0)
        return res