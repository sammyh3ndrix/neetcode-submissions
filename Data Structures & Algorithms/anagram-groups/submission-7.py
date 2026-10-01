class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anars = {

        }
        for words in strs:
            char = [0] * 26
            for i in words:
                char[ord(i) - ord("a")] = char[ord(i) - ord("a")] + 1
            tv = tuple(char)
            if tv in anars:
                anars[tv].append(words)
            else:
                anars[tv] = [words]
        return list(anars.values())
                
            