class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        r = len(numbers) - 1
        while i < r:
            total = numbers[i] + numbers[r]
            if total < target:
                i += 1
            elif total > target:
                r -= 1
            else:
                return [i + 1, r + 1]
        