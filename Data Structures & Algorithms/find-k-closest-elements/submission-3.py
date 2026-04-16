class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # so the array is sorted
        # the final answer is size k
        # answer is a subarray from the array as it is sorted 
        # left = 0, right = len(nums)-k
        # For a candidate start mid, should the best window be:
        # arr[mid : mid+k] or to the left side
        # or
        # something to the right of it?
        # a sub array that are cloeset to k
        # we have arr[mid: mid+k] win1
        # and we have arr[mid+1: mid+k+1] win2
        # notice win 1 and win2 overlaps except arr[mid] from win1 and arr[mid+k] from win2
        # we need to compare those two to decide
        # is it worth it to move to the right subarray?
        # or is it left is subarray is good

        left, right = 0 , len(arr)-k

        while left < right:
            mid = left + (right-left)//2

            if x - arr[mid] > arr[mid + k] - x:
                left = mid +1# move to the right
            else:
                right = mid

        return arr[left: left+k]