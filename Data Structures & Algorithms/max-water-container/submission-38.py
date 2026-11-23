class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        ret = 0
        while left < right:
            w = right - left
            h = min(heights[right], heights[left])
            a = h*w
            ret = max(ret,a)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return ret
        