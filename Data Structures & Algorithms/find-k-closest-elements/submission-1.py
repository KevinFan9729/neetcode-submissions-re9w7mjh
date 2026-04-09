class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # ok the array is sorted
        # closest elements are in a contigous subarray!
        # two pointer and shrink window size k
        # Time O(n)
        # Space O(1)
        left, right = 0, len(arr) - 1
        while left <= right:
            win_len = right - left + 1
            if win_len == k:
                break
            dist_left = abs(arr[left]-x)
            dist_right = abs(arr[right]-x)
            if dist_left <= dist_right:
                # left side is closer to x
                # shrink the window from the right side
                right -=1
            else:
                left +=1

        return arr[left:right+1]