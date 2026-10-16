class Solution:

    def encode(self, strs: List[str]) -> str:
        out = []
        for i in strs:
            enco = f"{len(i)}^{i}"
            out.append(enco)
        return "".join(out)
    def decode(self, s: str) -> List[str]:
        deco = []
        encofinder = 0
        while encofinder < len(s):
            delimfind = encofinder
            while s[delimfind] != "^":
                delimfind += 1
            length = int(s[encofinder:delimfind])
            startwrd = delimfind + 1
            endwrd = startwrd + length
            deco.append(s[startwrd:endwrd])
            encofinder = endwrd
        return deco
