class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        returns = []
        numsort = sorted(nums)
        for ind, val in enumerate(numsort):
            left = ind + 1
            right = len(numsort) - 1
            if ind > 0 and val == numsort[ind-1]:
                continue

            while left < right:
                if numsort[left] + numsort[right] + val < 0:
                    left += 1
                elif numsort[left] + numsort[right] + val > 0:
                    right -= 1
                else:
                    returns.append([val, numsort[left], numsort[right]])
                    left += 1
                    right -= 1
                    while left < right and numsort[left] == numsort[left-1]:
                        left += 1
        return returns

                
                    


               


        