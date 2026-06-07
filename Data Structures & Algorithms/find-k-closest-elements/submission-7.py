class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # we can have a shrinking sliding window
        # our objective is to shrink the window to size k
        # bec the array is sorted, those k elements are next to each other
        # Time O(n)
        # Space O(1)

        left, right = 0, len(arr) - 1

        while left < right:
            winLen = right - left + 1

            if winLen ==k:
                break

            leftLen = abs(arr[left] - x)
            rightLen = abs(arr[right] - x)
            if leftLen > rightLen:
                # the right is closer
                left += 1
            else:
                # the left is closer
                right -= 1
        
        return arr[left:right+1]