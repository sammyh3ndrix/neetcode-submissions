class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        iskiii = {}
        for ind, val in enumerate(nums):
            if target - val in iskiii:
                return [iskiii[target-val], ind]
            iskiii[val] = ind
        