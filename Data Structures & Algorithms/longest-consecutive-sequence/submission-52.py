class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        ret = 0
        for i in numset:
            if i - 1 not in numset:
                leng = 0
                while i + leng in numset:
                    leng += 1
                ret = max(ret, leng)
        return ret

        
        