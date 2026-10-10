class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers left and right to go thru the string from left and right 
        left = 0
        right = len(s) - 1
        # the pointers go thru the index psootions of the string thts why left starts at 0 and right starts at the lenegth of it - 1 meaning the end
        while left < right:
            #while the index psootion left is less then right index psootion meaning it will only run while both are traversing inward looking for whatver we are looking for
            while left < right and not s[left].isalnum():
                left += 1
                #whille left is less than right and the element is not alphanumeric then continue inward
            while left < right and not s[right].isalnum():
                right -= 1
                #while left is less than right and the right poointer is not alphanumerica mening numbers or alapahabet
            if s[left].lower() != s[right].lower():
                return False
                # returning false here becuase even if they are the same chacter the guidelies say its case senetisiitive so it has to be lower
            left += 1
            right -= 1
            # still incrmeneting for the puter while loop if the conditions in it are statsified 
        return True 
        #