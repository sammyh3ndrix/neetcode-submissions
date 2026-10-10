class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # setting tow poojnter ind1 and ind2 to go thru the array 
        ind1 = 0
        ind2 = len(numbers) - 1
        while ind1 < ind2:
            # always left is less than right becuase we are going inware iterating thru the indices of numbers 
            total = numbers[ind1] + numbers[ind2]
            #setting a varible total so we can compare the sum of the two indexes to target
            if total < target:
                ind1 += 1
                #if total is less than target then that means we need to increment our left pointer 1 posotion inward
            if total > target:
                ind2 -= 1
                # if total greater then tghat means its out the array so becuase ind2 is the number of th elentgh of the indices in the array so we need to incfrmenet - 1 on ind and keep moving inward 
            if total == target:
                return [ind1 + 1, ind2 + 1]
                # if total is equal then we return the indices the problem saus 1-indexed that means we need to add one to our return 

        