class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # two sum kinda like anagrams weherre we needs dicts but insetad of two dcits were only doing one to compare to nums
        i = {

        }

        #now we need to loops thru nums and get index and values using a for loop and enumrrae built in function
        for ind, val in enumerate(nums):
            #now we need to make sure find the intergers that equal to target lick for us its x[val] = index so were just gonna subtract our target from our value and check if its in the dicitorioanry we made for it
            if target - val in i:
                #now we need to return the array it asked for with the smaller index first we know the the smallewr index is target - val becuase we just used it to find the the bigger index i think????
                return [i[target - val], ind]
        #now we need to stroe every toher value that comes form the loop
            i[val] = ind
        