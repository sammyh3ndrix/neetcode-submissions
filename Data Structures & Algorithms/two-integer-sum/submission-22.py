class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        iski = {}
        for ind, val in enumerate(nums):
            if target - val in iski:
                return [iski[target - val], ind]
            iski[val] = ind