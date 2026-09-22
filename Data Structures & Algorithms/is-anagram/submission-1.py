class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        anat = {}
        anas = {}

        for i in range(len(s)):
            if s[i] in anas:
                anas[s[i]] = anas[s[i]] + 1
            else:
                anas[s[i]] = 1
            if t[i] in anat:
                anat[t[i]] = anat[t[i]] + 1
            else:
                anat[t[i]] = 1
        return anat == anas




        