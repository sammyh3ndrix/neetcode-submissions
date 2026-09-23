class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = {}
        for ind, val in enumerate(nums):
            if target - val in i:
                return [i[target-val], ind]
            i[val] = ind
        