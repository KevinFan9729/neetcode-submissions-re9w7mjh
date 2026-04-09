class Solution:
    def findMin(self, nums: List[int]) -> int:
        # array is right shifted 1 to n times
        # logn time we need some soft of binary search apporch
        # we may have two sections of the array
        # compare mid with right
        # if mid is smaller than right (we are in a sorted part of the array)
            # look for the left part
        # if mid is bigger than right (we are in an unsorted part of the array)
            # look for the right part
        # Time O(logn)
        # Space O(1)
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] < nums[right]:
                # we are in the sorted part of the array
                # check if this is the min
                    # i.e smaller than the num 1 setp left
                next_num_indx = max(mid - 1, 0)
                if nums[mid] < nums[next_num_indx]:
                    return nums[mid]
                # look for the left part of the array
                right = mid - 1
            elif nums[mid] > nums[right]:
                # we are in the unsorted part of the array
                # look for the right part of the array
                left = mid + 1
            else:
                return nums[mid]
        return nums[mid]