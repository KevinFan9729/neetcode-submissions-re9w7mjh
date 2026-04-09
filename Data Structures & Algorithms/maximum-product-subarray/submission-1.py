class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # O(n^2)
        # brute force
        product_ls = []
        for i in range(len(nums)-1, -1, -1):
            target_num = nums[i]
            product_ls.append(target_num)
            for j in range(i-1,-1, -1):
                last_product = product_ls[-1]
                last_product *= nums[j]
                product_ls.append(last_product)
        return max(product_ls)