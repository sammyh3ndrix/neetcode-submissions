class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += f"{len(word)}#{word}"
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            leng = int(s[i:j])
            start = j + 1
            end = start + leng
            decoded.append(s[start:end])
            i = end
        return decoded
