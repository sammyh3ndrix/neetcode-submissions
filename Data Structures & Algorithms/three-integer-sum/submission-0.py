class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        returns = []

        for ind, val in enumerate(nums):
            if ind > 0 and val == nums[ind - 1]:
                continue

            left = ind + 1
            right = len(nums) - 1

            while left < right:
                sums = nums[left] + nums[right] + val

                if sums < 0:
                    left += 1
                elif sums > 0:
                    right -= 1
                else:
                    returns.append([val, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return returns