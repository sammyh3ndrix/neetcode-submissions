class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        lval = 0
        rval = 0
        ret = 0
        while left < right:
            if height[left] <= height[right]:
                lval = max(lval, height[left])
                ret += lval - height[left]
                left += 1
            else:
                rval = max(rval, height[right])
                ret += rval - height[right]
                right -= 1
        return ret
        