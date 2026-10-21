class Solution:

    def encode(self, strs: List[str]) -> str:
        out = []
        for i in strs:
            enco = f"{len(i)}<{i}"
            out.append(enco)
        return "".join(out)

    def decode(self, s: str) -> List[str]:
        startenc = 0
        out = []
        while startenc < len(s):
            delim = startenc
            while delim < len(s) and s[delim] != "<":
                delim += 1
            startwrd = delim + 1
            leng = int(s[startenc:delim])
            endwrd = startwrd + leng
            out.append(s[startwrd:endwrd])
            startenc = endwrd
        return out

