class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {

        }
        for ind, val in enumerate(nums):
            if target - val in d:
                return [d[target - val], ind]
            d[val] = ind