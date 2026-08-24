class MinStack:

    def __init__(self):
        self.minVal = 2**31-1
        self.stack = []
        self.size = 0
        

    def push(self, val: int) -> None:
        if val < self.minVal:
           self.minVal = val
        self.stack.append([val, self.minVal])
        self.size += 1
        

    def pop(self) -> None:
        self.stack.pop(-1)
        self.size -= 1
        if self.size == 0:
            self.minVal = 2**31-1
        else:
            self.minVal = self.stack[-1][1]
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]

        
