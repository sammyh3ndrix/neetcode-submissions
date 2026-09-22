class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #return true if any value appears mroe than once in the array num with intergeres
        #relativly easy all thats needed is to create a hash set of nums then compre that hash set if it equals to oorginals nums array 
        return len(set(nums)) != len(nums)
        