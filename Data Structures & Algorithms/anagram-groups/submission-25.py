class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        iski = {}
        for words in strs:
            char = [0] * 26
            for i in words:
                char[ord(i) - ord("a")] = char[ord(i) - ord("a")] +1
            key = tuple(char)
            if key in iski:
                iski[key].append(words)
            else:
                iski[key] = [words]
        return list(iski.values())

        