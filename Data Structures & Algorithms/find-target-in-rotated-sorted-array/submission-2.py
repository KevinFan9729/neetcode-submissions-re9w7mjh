class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # log n means we need to do binary search
        # the array after rotation may have two sorted parts
        # one sorted part is bigger than the other
        # maybe we need to do comparsions?
            # 1 check which part of sorted array you are in right now
            # 2 check if the target is in the sorted arrray that you are in
        # Time O(logn)
        # Space O(1)
        
        left, right = 0, len(nums)-1

        while left <=right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid

            #  [mid..right] is sorted
            if nums[mid] < nums[right]:
                if target == nums[right]:
                    return right
                if nums[mid] < target < nums[right]:
                    # target is in this sorted range
                    # look at is sorted range
                    left = mid + 1
                else:
                    # target is NOT In [mid...right]
                    right = mid - 1
            # [left...mid] is sorted
            else:
                if target == nums[left]:
                    return left
                if nums[left] < target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1
        