class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ret = []
        for i in tokens:
            if i not in ["-", "/", "*", "+"]:
                ret.append(int(i))
            else:
                right = ret.pop()
                left = ret.pop()
                if i == "/":
                    ret.append(int(left/right))
                elif i == "*":
                    ret.append(left*right)
                elif i == "+":
                    ret.append(left+right)
                elif i == "-":
                    ret.append(left-right)
        return ret[-1]
        