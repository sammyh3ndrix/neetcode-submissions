class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        run = 1
        for i in nums:
            out.append(run)
            run *= i
        run = 1
        for i in range(len(nums)-1, -1, -1):
            out[i] *= run
            run *= nums[i]
        return out

        