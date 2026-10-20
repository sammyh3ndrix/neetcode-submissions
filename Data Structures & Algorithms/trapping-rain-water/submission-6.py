class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        lvalh = 0
        rvalh = 0
        tot = 0
        while left < right:
            if height[left] <= height[right]:
                lvalh = max(lvalh, height[left])
                tot += lvalh - height[left]
                left += 1
            else:
                rvalh = max(rvalh, height[right])
                tot += rvalh - height[right]
                right -= 1
        return tot
                