class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        leng = 0
        numset = set(nums)
        for i in numset:
            if i - 1 not in numset:
                wrd = 0
                while wrd + i in numset:
                    wrd += 1
                leng = max(wrd, leng)
        return leng
        