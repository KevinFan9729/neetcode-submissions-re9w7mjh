class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # a rectangle is area is computed as length * width
        # we want to find the max area
        # we cannot sort, that will destroy the order of the "wall"
        # in term of height, the shorter height is the restricting one
        # in term of the width, we want the max width (furthest) possible
        # two pointers with running maxArea tracking
        # Time O(n)
        # Space O(1)

        left, right = 0, len(heights) - 1
        max_area = 0
        while left < right:
            width = right - left
            if heights[left] < heights[right]:
                # the shorter wall is the limiting factor
                height = heights[left]
                left += 1
            elif heights[left] > heights[right]:
                height = heights[right]
                right -= 1
            else:# when we have a tie
                # we can advance either pointer
                # this does not matter as the largest possible area with longer width is recorded regardless
                # width is shrinking monotonically and we always keep the max area seen so far
                height = heights[left]
                left += 1
            max_area = max(max_area, width*height)
        return max_area