class MinStack:

    def __init__(self):
        self.min_stack = []


    def push(self, val: int) -> None:
        if len(self.min_stack) <= 0:
            self.min_stack.append(val)
        elif val <= self.min_stack[0]:
            self.min_stack.insert(0, val)
        self.min_stack.append(val)


    def pop(self) -> None:
        if self.min_stack[-1] == self.min_stack[0]:
            self.min_stack.pop(0)
        self.min_stack.pop()


    def top(self) -> int:
        return self.min_stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[0]

    
    def size(self):
        return len(self.min_stack)
        
