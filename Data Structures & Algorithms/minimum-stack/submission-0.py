class MinStack:

    def __init__(self):
        self.minVal = 0
        self.size = 0
        self.stack = []
        

    def push(self, val: int) -> None:
        if self.size == 0:
            self.minVal = val
        elif val < self.minVal:
           self.minVal = val
        self.stack.append(val)
        self.size += 1
        

    def pop(self) -> None:
        self.stack.pop(-1)
        self.size -= 1
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return min(self.stack)

        
