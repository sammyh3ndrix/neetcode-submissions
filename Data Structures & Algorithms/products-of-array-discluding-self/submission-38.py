class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        run = 1
        for i in nums:
            res.append(run)
            run *= i
        run = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= run
            run*= nums[i]
        return res