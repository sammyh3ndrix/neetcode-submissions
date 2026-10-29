class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        iski = {}
        for words in strs:
            char = [0] * 26
            for i in words:
                char[ord(i) - ord("a")] = char[ord(i) - ord("a")] + 1
            keys = tuple(char)
            if keys in iski:
                iski[keys].append(words)
            else:
                iski[keys] = [words]
        return list(iski.values())

        