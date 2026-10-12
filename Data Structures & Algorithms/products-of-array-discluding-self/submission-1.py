class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        output = []
        running = 1
        for i in nums:
            prefix.append(running)
            running *= i
        running = 1
        for i in range(len(nums)-1, -1, -1):
            suffix.append(running)
            running *= nums[i]
        suffix.reverse()
        for i in range(len(nums)):
            output.append(prefix[i] * suffix[i])
        return output
        
        