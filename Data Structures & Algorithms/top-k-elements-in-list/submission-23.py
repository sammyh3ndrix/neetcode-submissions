class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        iski = {}
        for i in nums:
            if i in iski:
                iski[i] += 1
            else:
                iski[i] = 1
        buckets = [[]for _ in range(len(nums)+1)]
        for num, freq in iski.items():
            buckets[freq].append(num)
        results = []
        for i in range(len(buckets)-1, -1, -1):
            for numbers in buckets[i]:
                results.append(numbers)
                if len(results) == k:
                    return results

        