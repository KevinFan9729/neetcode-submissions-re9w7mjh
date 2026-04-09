class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # std alg
        # the list is sorted; so we can do binary search
        # assume the number at the middle is the target
        # if mid is smaller than the target -> look at the right portion
        # if the mid is bigger than the target -> look at the left portion
        # Time O(logn) reduce the search space by half every step
        # space O(1)
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (right + left)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
            else:
                return mid
        return -1