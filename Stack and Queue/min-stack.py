# Leet Code link : https://leetcode.com/problems/min-stack/


class MinStack:

    def __init__(self):
        self.stack = []
        self .m = 0
        self.m1 = 0
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.stack == None:
            self.m = val
            self.m1 = val
        else:
            self.m1 = self.m
            self.m = min(self.m, val) 

    def pop(self) -> None:
        if self.stack == None:
            return None
        else:
            self.m = self.m1
            return self.stack.pop()  
            
    def top(self) -> int: 
        return self.stack[len(self.stack)-1]
        
    def getMin(self) -> int:
        return self.m


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
