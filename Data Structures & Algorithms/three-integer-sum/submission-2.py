
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numsort = sorted(nums)
        out = []

        for ind, val in enumerate(numsort):
            # Skip duplicate fixed numbers
            if ind > 0 and val == numsort[ind - 1]:
                continue

            left = ind + 1
            right = len(numsort) - 1

            while left < right:
                total = val + numsort[left] + numsort[right]

                if total < 0:
                    left += 1

                elif total > 0:
                    right -= 1

                else:
                    out.append([val, numsort[left], numsort[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and numsort[left] == numsort[left - 1]:
                        left += 1

        return out
