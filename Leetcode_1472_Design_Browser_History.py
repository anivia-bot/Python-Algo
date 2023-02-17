class Node:
    
    def __init__(self, val):
        self.data = val
        self.prev, self.next = None, None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.current = self.head

    def visit(self, url: str) -> None:
        newNode = Node(url)
        self.current.next = newNode
        newNode.prev = self.current
        self.current = newNode
        

    def back(self, steps: int) -> str:

        while steps > 0 and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        return self.current.data

    def forward(self, steps: int) -> str:
        
        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -= 1
        return self.current.data


