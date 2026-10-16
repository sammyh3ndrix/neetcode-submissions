class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = []
        for word in strs:
            encoded = f"{len(word)}#{word}"
            enc.append(encoded)
        return "".join(enc)



    def decode(self, s: str) -> List[str]:

        out = []
        lbegin = 0
        while lbegin < len(s):
            jdelimfind = lbegin
            while s[jdelimfind] != "#":
                jdelimfind += 1
            lentoextr = int(s[lbegin:jdelimfind])
            startwrdind = jdelimfind + 1
            endwrdind = lentoextr +  startwrdind
            out.append(s[startwrdind:endwrdind])
            lbegin = endwrdind
        return out







