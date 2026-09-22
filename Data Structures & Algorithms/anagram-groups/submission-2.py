class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anars = {}
        for words in strs:
            chars = [0] * 26
            for i in words:
                chars[ord(i) - ord("a")] = chars[ord(i) - ord("a")] + 1
            key = tuple(chars)
            if key in anars:
                anars[key].append(words)
            else:
                anars[key] = [words]

        return list(anars.values())


