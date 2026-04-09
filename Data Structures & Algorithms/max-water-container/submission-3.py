class Solution:
    def maxArea(self, height: List[int]) -> int:
        # we will use a two pointer method
        # the area is the area of a rectangle
            # area = width * height
                # width  = right - left 
                # height = min(height[left], height[right])
        # if either the left or the right is the limiting factor, 
        # we will move the respective pointer in hope of getting a better height

        maxArea = 0

        left, right = 0, len(height) -1

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            area = w * h
            maxArea = max(maxArea, area)
            if height[left] <= height[right]:
                left +=1
            else:
                right -=1
        return maxArea