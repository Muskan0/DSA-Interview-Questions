# https://leetcode.com/problems/min-stack/

# Design a stack that supports push, pop, top, and 
# retrieving the minimum element in constant time.

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.minEle=0
        
    def push(self, x: int) -> None:
        if self.top()==None:
            self.stack.append(x)
            self.minEle=x
        elif x<self.minEle:
            self.stack.append(2*x-self.minEle)
            self.minEle=x
        else:
            self.stack.append(x)

    def pop(self) -> None:
        if self.stack is not None:
            m=self.stack.pop()
            if m<self.minEle:
                self.minEle=2*self.minEle-m
            
    def top(self) -> int:
        if self.stack is None or self.stack==[]:
            return None
        m=self.stack[-1]
        if m>self.minEle:
            return m
        return self.minEle
        
    def getMin(self) -> int:
        return self.minEle

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
