from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n)
        # if we have two zeros, the entire answer is zero
        res = [0] * len(nums)
        found_zero = False
        zero_idx = -1
        product = 1

        for i, num in enumerate(nums):
            # seeing zero for the first time
            if num == 0 and not found_zero:
                found_zero = True
                zero_idx = i
                continue

            # seeing zero for the second time
            if num == 0:
                return res

            # normal non-zero number
            product *= num

        # there's a zero in nums, so all res is 0 except the idx of the zero
        if found_zero:
            res[zero_idx] = product
            return res

        # res[i] is the product divided by nums[i]
        for i in range(len(nums)):
            res[i] = product // nums[i]

        return res
