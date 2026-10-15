class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anars = {}
        for word in strs:
            char = [0] * 26
            for i in word:
                char[ord(i) - ord("a")] = char[ord(i) - ord("a")] + 1
            key = tuple(char)
            if key in anars:
                anars[key].append(word)
            else:
                anars[key] = [word]
        return list(anars.values())