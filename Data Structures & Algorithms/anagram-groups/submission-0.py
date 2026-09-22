class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anars = {}
        for word in strs:
            chars = [0] * 26
            for i in word:
                    chars[ord(i) - ord("a")] = chars[ord(i) - ord("a")] + 1
            key = tuple(chars)

            if key in anars:
                anars[key].append(word)
            else:
                anars[key] = [word]

        return list(anars.values())





        