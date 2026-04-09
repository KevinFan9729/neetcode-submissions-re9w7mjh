# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # binary search
        # the number range is 1 to n
        # Time O(logn)
        # Space O(1)

        left, right = 1, n

        while left <= right:
            mid = left+ (right-left)//2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == -1:
                # guess is higher than the target
                right = mid-1
            else:
                left = mid+1