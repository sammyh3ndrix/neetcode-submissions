class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        mx = 0
        for i in nums:
            if i - 1 not in numset:
                leng = 0
                while leng + i in numset:
                    leng += 1
                mx = max(leng,mx)
        return mx
        