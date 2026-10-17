class Solution:

    def encode(self, strs: List[str]) -> str:
        neco = []
        for i in strs:
            enc = f"{len(i)}^{i}"
            neco.append(enc)
        return "".join(neco)
    def decode(self, s: str) -> List[str]:
        startenc = 0
        out = []
        while startenc < len(s):
            delim = startenc
            while s[delim] != "^":
                delim += 1
            lengwrd = int(s[startenc:delim])
            startwrd = delim + 1
            endwrd = lengwrd + startwrd
            out.append(s[startwrd:endwrd])
            startenc = endwrd
        return out
