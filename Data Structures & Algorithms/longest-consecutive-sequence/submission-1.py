class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setski = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in setski:
                length = 1
                while num + length in setski:
                    length += 1
                longest =  max(longest, length)
        return longest
        