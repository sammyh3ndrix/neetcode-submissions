class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idd = 0
        idx = len(numbers) - 1
        while idd < idx:
            total = numbers[idd] + numbers[idx]
            if total < target:
                idd += 1
            elif total > target:
                idx -= 1
            else:
                return [idd + 1, idx + 1]
        