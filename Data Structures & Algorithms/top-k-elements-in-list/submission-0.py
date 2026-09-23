class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for val in nums:
            if val in freq:
                freq[val] = freq[val] + 1
            else:
                freq[val] = 1
        buckets = [[]for i in range(len(nums) + 1)]
        for key, val in freq.items():
            buckets[val].append(key)
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

