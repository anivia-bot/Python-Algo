class MinStack:
    
    # All operation should be run in O(1) time O(N) space
    # The trick is to have 2 equal length array. One track the regular stack and the other track the minStack

    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        
        else:
            smallestVal = min(self.minStack[-1], val)
            self.minStack.append(smallestVal)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()