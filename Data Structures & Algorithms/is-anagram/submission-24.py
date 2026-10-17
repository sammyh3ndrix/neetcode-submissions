class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ans = {}
        ant = {}
        for i in range(len(s)):
            if s[i] in ans:
                ans[s[i]] += 1
            else:
                ans[s[i]] = 1
            if t[i] in ant:
                ant[t[i]] += 1
            else:
                ant[t[i]] = 1
        return ant == ans