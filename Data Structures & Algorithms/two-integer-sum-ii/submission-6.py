class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ind1 = 0
        ind2 = len(numbers) - 1
        while ind1 < ind2:
            total = numbers[ind1] + numbers[ind2]
            if total < target:
                ind1 += 1
            elif total > target:
                ind2 -= 1
            else:
                return [ind1 + 1, ind2 + 1]

        