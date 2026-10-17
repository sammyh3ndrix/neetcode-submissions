class Solution:
    def trap(self, height: List[int]) -> int:
        totwat = 0
        left = 0
        right = len(height) - 1
        lmxhe = 0
        rmxhe = 0
        while left < right:
            if height[left] <= height[right]:
                lmxhe = max(height[left], lmxhe)
                totwat += lmxhe - height[left]
                left += 1
            else:
                rmxhe = max(height[right], rmxhe)
                totwat += rmxhe - height[right]
                right -= 1
        return totwat

