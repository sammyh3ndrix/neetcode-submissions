class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # varible lonegest is global count of what we are returning
        longest = 0
        # numset is because the secuaunce needs to have elements exactly 1 greater than previcuos element this makes so theres no duplicates
        numset = set(nums)
        for i in numset:
            if i - 1 not in numset:
                # this condiitonal is just checking to make sure that the element i we aere on has nothing less than in the numset i think??
                length = 0
                #this varible lentgh is to start a local count of cosenescutue sequences we will compare this with longest then return the bigger one
                while i + length in numset:
                    length += 1
                longest = max(longest, length)
        return longest
        