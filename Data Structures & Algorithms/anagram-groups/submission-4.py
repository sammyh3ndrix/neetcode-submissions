class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anars = {}
        for words in strs:
            char = [0] * 26
            for i in words:
                char[ord(i) - ord("a")] = char[ord(i) - ord("a")] + 1
            key = tuple(char)
            if key in anars:
                anars[key].append(words)
            else:
                anars[key] = [words]
        return list(anars.values())
        