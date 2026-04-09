class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # more than 2 zeros then the result will be zero for all pos
        # we can compute two arrays
        # one forward product array
        # one backward product array
        # to compute the product of array except at pos i
            # forward[i-1] * backward[i+1]
        # just need to watch out for index out of bound
        # time O(n)
        # space O(n)

        # compute the forward array
        forward_prod = [0] * len(nums)
        backward_prod = [0] * len(nums)
        res = [0] * len(nums)
        forward_prod[0] = nums[0]
        backward_prod[-1] = nums[-1]

        for i in range(1,len(nums)):
            forward_prod[i] = forward_prod[i-1] * nums[i]
            backward_prod[len(nums)-1 -i] = backward_prod[len(nums) -i]* nums[len(nums)-1 -i]
        for i in range(len(nums)):
            fwd_idx = i-1
            bwd_idx = i+1
            fwd_prod = 1
            bwd_prod = 1
            if fwd_idx >= 0:
                fwd_prod = forward_prod[fwd_idx]
            if bwd_idx < len(nums):
                bwd_prod = backward_prod[bwd_idx]
            res[i] = fwd_prod * bwd_prod

        return res
