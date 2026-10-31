class MinStack:

    def __init__(self):
        self.stack = []
        self.minst = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minst:
            self.minst.append(val)
        else:
            self.minst.append(min(self.minst[-1], val))      

    def pop(self) -> None:
        self.minst.pop()
        self.stack.pop()

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minst[-1]
        
