class Solution:

    def encode(self, strs: List[str]) -> str:
        enco = []
        for i in strs:
            enc = f"{len(i)}#{i}"
            enco.append(enc)
        return "".join(enco)

    def decode(self, s: str) -> List[str]:
        output = []
        startenc = 0
        while startenc < len(s):
            delim = startenc
            while s[delim] != "#":
                delim += 1
            lengwrd = int(s[startenc:delim])
            startwrd = delim + 1
            endwrd = lengwrd + startwrd
            output.append(s[startwrd:endwrd])
            startenc = endwrd
        return output