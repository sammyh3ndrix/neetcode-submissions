class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        iski = {}

        # 1. Count frequencies
        for i in nums:
            if i in iski:
                iski[i] += 1
            else:
                iski[i] = 1

        # 2. Create frequency buckets
        bucket = [[] for _ in range(len(nums) + 1)]

        # 3. Place numbers into buckets by frequency
        for num, freq in iski.items():
            bucket[freq].append(num)

        # 4. Collect the k most frequent numbers
        ret = []
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                ret.append(num)
                if len(ret) == k:
                    return ret