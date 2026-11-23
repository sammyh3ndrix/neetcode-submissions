class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        iski = {}
        for i in nums:
            if i in iski:
                iski[i] +=1
            else:
                iski[i]     = 1
        bucket = [[]for _ in range(len(nums)+1)]
        for num, freq in iski.items():
            bucket[freq].append(num)
        res = []
        for i in range(len(bucket)-1, -1, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
    