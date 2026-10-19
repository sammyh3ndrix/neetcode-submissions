class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        run = 1
        out = []
        for u in nums:
            out.append(run)
            run *= u
        run = 1
        for u in range(len(nums)-1, -1 ,-1):
            out[u] *= run
            run *= nums[u]
        return out        