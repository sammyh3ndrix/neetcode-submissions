class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        mac = 0
        for i in numset:
            if i - 1 not in numset:
                length = 0
                while length + i in numset:
                    length += 1
                mac = max(mac, length)
        return mac
        