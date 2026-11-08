class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        run = 1
        glb = []
        for i in nums:
            glb.append(run)
            run *= i
        run = 1
        for i in range(len(nums)-1,-1,-1):
            glb[i] *= run
            run *= nums[i]
        return glb
      
            


        