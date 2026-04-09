class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # O(n^2) solution
        # width = right_index - left_index
        # height = min(heights[left_index], heights[right_index])
        # area = height * width
        # number of iterations of the loop (n-1) + (n-2) + (n-3)+ ...+ 1 = n(n-1)/2 = O(n^2)
        if len(heights) == 2:
            width = 1
            height = min(heights[0], heights[1])
            area = height * width
            return area
        left, right = 0, len(heights)-1
        max_area = 0
        while right >= 1:
            while left < right:
                width = right - left
                height = min(heights[left], heights[right])
                area = height * width
                if area > max_area:
                    max_area = area
                left += 1
            left = 0 # reset left pointer
            right -= 1
        return max_area