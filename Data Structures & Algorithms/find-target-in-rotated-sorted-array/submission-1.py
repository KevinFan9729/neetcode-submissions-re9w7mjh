class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # must use binary search to get to O(logn)
        def inflectionIndex(nums: List[int]) -> int:
            # we actually have two sorted arrays due to rotation
            # the left part and the right part
            # the left part array are greater than the right part array
            # we will try to find the point of inflection 
            left, right = 0 , len(nums) -1
            while left < right:
                mid = left + (right-left)//2
                if nums[mid]>nums[(mid-1)] and nums[(mid+1)]<nums[mid]: #inflection point
                    return mid+1
                elif nums[mid] > nums[right]:
                    left = mid
                else:
                    right = mid
            return 0 # if we are here, that means there is no inflection point, (we have no right subarray)
        def binarySearch(nums: List[int], target: int):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = left + (right-left)//2
                if nums[mid] >target: # need to search left side
                    right = mid -1
                elif nums[mid] < target: # need to search right side
                    left = mid + 1
                else:
                    return mid
            return -1
        inflectionIdx = inflectionIndex(nums)
        searchFirst = binarySearch(nums[0:inflectionIdx], target)
        if searchFirst != -1:
            return searchFirst
        searchSec = binarySearch(nums[inflectionIdx:], target)
        if searchSec != -1:
            return searchSec + inflectionIdx
        return -1


