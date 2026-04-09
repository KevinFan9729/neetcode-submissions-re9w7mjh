class Solution:
    def mySqrt(self, x: int) -> int:
        # sqrt is of a is b*b = a 
        # in this case we just need to find a value b which the product is
        # less than a
        # cloest to a
        # think about the search space
        # binary search?
        # really we are looking for a num which is the inflection point
            # product of this num is equal to the target
            # or
            # product of this num is less than the target and anything byond this num has product larger than the target
        # Time O(logn)
        # Space O(1)
        if x == 0:
            return 0
        if x == 1:
            return 1
        
        left = 1
        right = x//2
        while left <=right:
            mid = left + (right-left)//2
            print(mid)
            prod = mid*mid
            if prod == x:
                return mid
            elif prod < x:
                left= mid+1
            else:
                right = mid-1
        # after our loop ends, it means left > right
        # this means our inflection point is right (as we round down here)
        return right

        