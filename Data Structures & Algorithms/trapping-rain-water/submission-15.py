class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        lval = 0
        rval = 0
        tot =0
        while l < r:
            if height[l] <= height[r]:
                lval = max(height[l], lval)
                tot += lval - height[l]
                l += 1
            else:
                rval = max(height[r], rval)
                tot += rval - height[r]
                r -= 1
        return tot