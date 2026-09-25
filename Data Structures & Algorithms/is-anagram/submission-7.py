class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        anas = {}
        anat = {}

        for val in range(len(t)):
            if t[val] in anat:
                anat[t[val]] = anat[t[val]] + 1
            else:
                anat[t[val]] = 1
            if s[val] in anas:
                anas[s[val]] = anas[s[val]] + 1
            else:
                anas[s[val]] = 1
        return anas == anat

        