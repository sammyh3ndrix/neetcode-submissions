class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        run = 1
        output = []
        for val in nums:
            output.append(run)
            run *= val
        run = 1
        for val in range(len(nums)-1, -1, -1):
            output[val] *= run
            run *= nums[val]
        return output