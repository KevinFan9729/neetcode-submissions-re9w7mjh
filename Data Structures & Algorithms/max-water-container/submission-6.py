class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # shrinking window
        # if one side is smaller then we shirnk from this side in search of a bigger length
        # what if both sides are equal in length?
            # does not matter to shirnk from which side
            # why
            # say letf and right wall are the same height
            # Now consider any future container that still uses the left wall but moves the right wall inward:
            # its width is smaller
            # its height is at most h, because the left wall is still height h
            # So it cannot beat the current area.
            # Therefore, it is safe to discard the left wall. By the same reasoning, it would also be safe to discard the right wall. length situation do not give you the maxArea; shrinking from either side will arrive at the max area
        # Time O(n)
        # Space O(1)
        left, right = 0 , len(heights)-1
        maxArea = 0
        while left < right:
            length = right - left
            if heights[left] <= heights[right]:
                height = heights[left]
                left+=1
            else:
                height = heights[right]
                right-=1
            maxArea = max(maxArea, length*height)
        return maxArea           