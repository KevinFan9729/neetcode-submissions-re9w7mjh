class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) -1
        max_area = 0
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height
            if area > max_area:
                max_area = area
            if heights[left] > heights[right]:
                right -=1
            else:
                left += 1
        return max_area

        