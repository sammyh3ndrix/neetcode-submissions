class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        x = len(numbers) - 1
        while i < x:
            total = numbers[i] + numbers[x]
            if total < target:
                i += 1
            elif total > target:
                x -= 1
            else:
                return [i + 1, x + 1]
        