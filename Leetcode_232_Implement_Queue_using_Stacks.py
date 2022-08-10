class MyQueue:
    
    '''
    For pop and peek it runs in O(1) amortized. push and empty are both O(1)
    Since we are having two stacks that would store up the entire Queue
    The Space complexity would be O(N)
    '''

    def __init__(self):
        self.pushStack = []
        self.popStack = []

    def push(self, x: int) -> None:
        self.pushStack.append(x)

    def pop(self) -> int:
        if not self.popStack:
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())
        return self.popStack.pop()
                

    def peek(self) -> int:
        if not self.popStack:
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())
        return self.popStack[-1]
        

    def empty(self) -> bool:
        return not self.pushStack and not self.popStack
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()