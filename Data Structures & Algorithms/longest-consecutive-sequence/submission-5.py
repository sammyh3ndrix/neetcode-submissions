class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numski = set(nums)
        longest = 0
        for num in numski:
            if num - 1 not in numski:
                length = 0
                while num + length in numski:
                    length += 1
                longest = max(longest, length)
        return longest
        