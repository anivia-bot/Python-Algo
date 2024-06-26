class Node:
    
    def __init__(self, val):
        self.data = val
        self.prev, self.next = None, None

class BrowserHistory:

    def __init__(self, homepage):
        self.head = Node(homepage)
        self.current = self.head

    def visit(self, url):
        newNode = Node(url)
        self.current.next = newNode
        newNode.prev = self.current
        self.current = newNode
        

    def back(self, steps):

        while steps > 0 and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        return self.current.data

    def forward(self, steps):
        
        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -= 1
        return self.current.data


