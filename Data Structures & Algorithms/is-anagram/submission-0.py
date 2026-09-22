class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      st = s.lower()
      ts = t.lower()
      if len(st) != len(ts):
        return False
      return sorted(st) == sorted(ts)


        