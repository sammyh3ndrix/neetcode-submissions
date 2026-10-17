class Solution:
    def trap(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        lheightmx = 0
        rheightmx = 0
        totwat = 0
        while left < right:
            if height[left] <= height[right]:
                lheightmx = max(lheightmx, height[left])
                totwat += lheightmx - height[left]
                left += 1
            else:
                rheightmx = max(rheightmx, height[right])
                totwat += rheightmx - height[right]
                right -= 1
        return totwat






        