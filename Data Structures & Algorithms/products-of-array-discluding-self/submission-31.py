class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = []
        run = 1
        for i in nums:
            ret.append(run)
            run *= i
        run = 1
        for i in range(len(nums)-1,-1,-1):
            ret[i] *= run
            run *= nums[i]
        return ret
        