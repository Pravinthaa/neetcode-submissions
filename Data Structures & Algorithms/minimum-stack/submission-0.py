class MinStack:

    def __init__(self):
        self.stack=[]
        self.mins=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins:
            self.mins.append(val)
        else:
            a=min(val,self.mins[-1])
            self.mins.append(a)
        

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

        

    def top(self) -> int:
        i=self.stack[-1]
        return i
        

    def getMin(self) -> int:
        return self.mins[-1]
        
