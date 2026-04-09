class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # If the mid element is greater than the right element, the minimum is in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Otherwise, the minimum is in the left half (including mid)
                right = mid
        
        # The left pointer will point to the minimum element
        return nums[left]
