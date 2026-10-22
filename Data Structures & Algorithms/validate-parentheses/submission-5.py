class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:
            if char in "([{":
                st.append(char)
            else:
                if not st or st[-1] != pairs[char]:
                    return False
                st.pop()

        return len(st) == 0