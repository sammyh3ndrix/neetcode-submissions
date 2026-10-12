class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        globe = 0
        right = len(heights) - 1
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height
            globe = max(globe, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return globe
        