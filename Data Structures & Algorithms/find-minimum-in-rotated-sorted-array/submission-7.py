class Solution:
    def findMin(self, nums: List[int]) -> int:
        # log n means we need to do binary search
        # the array after rotation MAY have two sorted parts
        # Time O(logn)
        # Space O(1)

        left, right = 0, len(nums) -1
        ans = nums[0]
        while left <= right:
            mid = left+(right-left)//2
            if nums[mid] < nums[right]:
                # [mid...right] is sorted!
                # we are looking for the min
                # so mid possibly be min
                ans = min(ans, nums[mid])
                # now look at the left side
                # to continue the search
                right = mid - 1
            else:
                # [left...mid] is sorted!
                # left may be the possible min
                ans = min(ans, nums[left])
                # look at the other side
                # we don't know which side actually smaller!
                # so we need to continue the search
                left = mid + 1
        return ans

