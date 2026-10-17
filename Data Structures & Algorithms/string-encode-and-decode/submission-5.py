class Solution:

    def encode(self, strs: List[str]) -> str:
        neco = []
        for words in strs:
            enc = f"{len(words)}>{words}"
            neco.append(enc)
        return "".join(neco)

    def decode(self, s: str) -> List[str]:
        out = []
        startenc = 0
        while startenc < len(s):
            delim = startenc
            while s[delim] != ">":
                delim += 1
            lengwrd = int(s[startenc:delim])
            startwrd = delim + 1
            endwrd = lengwrd + startwrd
            out.append(s[startwrd:endwrd])
            startenc = endwrd
        return out
