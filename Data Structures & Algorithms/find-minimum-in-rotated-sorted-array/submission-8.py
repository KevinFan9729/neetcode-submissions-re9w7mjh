class Solution:
    def findMin(self, nums: List[int]) -> int:
        # base on the time complexity
        # it needs a binary search apporch
        # we have two sorted portion at most
        # or one sorted portion
        # if mid is smaller than right
            # mid is in a sorted portion
            # answer maybe in the left
            # also mid may be the min
        # if mid is bigger than the right
            # mid is in another sorted portion
            # answer maybe in the right
        # Time O(logn)
        # Space O(1)

        left, right = 0 , len(nums)-1

        while left <= right:
            mid = left + (right-left)//2
            print(left, right, mid)
            if nums[mid] < nums[right]:
                # mid could be the min, so mid inclusive
                right = mid
            elif nums[mid] > nums[right]:
                left = mid +1
            else:
                return nums[mid]
        return nums[left]