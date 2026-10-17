class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        lhemx = 0
        rhemx = 0
        totwat = 0
        while left < right:
            if height[left] <= height[right]:
                lhemx = max(lhemx,height[left])
                totwat += lhemx - height[left]
                left += 1
            else:
                rhemx = max(rhemx,height[right])
                totwat += rhemx - height[right]
                right -= 1
        return totwat

        