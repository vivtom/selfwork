class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mini.append(min(val,self.mini[-1] if self.mini else val))

    def pop(self) -> None:
        self.stack.pop()
        self.mini.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini[-1]