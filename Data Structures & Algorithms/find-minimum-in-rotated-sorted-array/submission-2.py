class Solution:
    def findMin(self, nums: List[int]) -> int:
        # we actually have two sorted arrays due to rotation
        # the left part and the right part
        # the left part array are greater than the right part array
        # we will try to find the point of reflection 
        left, right = 0 , len(nums) -1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid]>nums[(mid-1)] and nums[(mid+1)]<nums[mid]: #reflection point
                return nums[(mid+1)]
            elif nums[mid] > nums[right]:
                left = mid
            else:
                right = mid
        
        return nums[0] # if we are here, that means there is no reflection point, (we have no right subarray)
            