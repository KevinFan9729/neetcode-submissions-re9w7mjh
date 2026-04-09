class Solution:
    def findMin(self, nums: List[int]) -> int:
        # we actually have two sorted arrays due to rotation
        # the left part and the right part
        # the left part array are greater than the right part array
        length = len(nums)
        left, right = 0 , length -1
        while left < right:
            mid = left + (right-left)//2
            left_val = nums[left]
            right_val = nums[right]
            mid_val = nums[mid]
            if nums[mid]>nums[(mid-1)%length] and nums[(mid+1)%length]<nums[mid]: #reflection point
                return nums[(mid+1)%length]
            elif nums[mid] > nums[right]:
                left = mid
            else:
                right = mid
        
        return nums[0]
            