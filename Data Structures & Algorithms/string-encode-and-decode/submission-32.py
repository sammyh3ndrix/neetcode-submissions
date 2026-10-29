class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = []
        for i in strs:
            enco = f"{len(i)}^{i}"
            enc.append(enco)
        return "".join(enc)

    def decode(self, s: str) -> List[str]:
        out = []
        startenc = 0
        while startenc < len(s):
            delim = startenc
            while delim < len(s) and s[delim] != "^":
                delim += 1
            startwrd = delim + 1
            lengwrd = int(s[startenc:delim])
            endwrd = startwrd + lengwrd
            out.append(s[startwrd:endwrd])
            startenc = endwrd
        return out
