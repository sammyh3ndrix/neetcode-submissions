class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        iski = {}
        for ele in nums:
            if ele in iski:
                iski[ele] += 1
            else:
                iski[ele] = 1
        buckets = [[]for _ in range(len(nums) + 1)]
        for num, freq in iski.items():
            buckets[freq].append(num)
        results = []
        for i in range(len(buckets)-1, -1, -1):
            for number in buckets[i]:
                results.append(number)
            if len(results) == k:
                return results
        