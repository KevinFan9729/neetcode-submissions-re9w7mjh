class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = []
        for i in range(len(nums)-1, -1, -1):
            target_num = nums[i]
            dp.append(target_num)
            for j in range(i-1,-1, -1):
                last_product = dp[-1]
                last_product *= nums[j]
                dp.append(last_product)
        return max(dp)