class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        for ind, val in enumerate(nums):
            if ind > 0 and val == nums[ind-1]:
                continue
            left = ind + 1
            right = len(nums) - 1
            while left < right:
                total = nums[left] + nums[right] + val
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    out.append([nums[left], nums[right], val])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        return out
        