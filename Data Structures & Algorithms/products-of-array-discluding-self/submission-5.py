class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        run = 1
        for i in nums:
            output.append(run)
            run *= i
        run = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= run
            run *= nums[i]
        return output
        