class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        lvalh = 0 
        rvalh = 0
        totwat = 0
        while left < right:
            if height[left] <= height[right]:
                lvalh = max(height[left], lvalh)
                totwat += lvalh - height[left]
                left += 1
            else:
                rvalh = max( height[right], rvalh)
                totwat += rvalh - height[right]
                right -= 1
        return totwat

        