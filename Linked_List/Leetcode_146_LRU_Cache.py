'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement the LRUCache class:
LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. 
Otherwise, add the key-value pair to the cache. 
If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]
'''
'''
Solution:

LRU cache you need to think of linked list right away
First set a new class called Node as we will store key, val, prev and next variable in it

Second create a cache hash map and create a a left and right node.
The left node will be pointing at the least used cahce and the right will be the 
most recent used cache. Set left and right to be pointing at each other to form a 
doubly linked list

Third create an insert and remove function for us to implement the algo easily

Fourth the get function will return the val if its in cache. Once this has been done
remove the val from the cache and insert it on the right hand side

Fifth the put function will insert a value to the cache and 
make them be connect to the right ptr (most recent used)

if the cache exceed capacity then just remove the lru (self.left.next)
and remove it from the cache dict as well 

In sum, initialize left and right to trakc least lru and most recent lru
Use a dict to save all cache
create an extra node to be able to connect on the linked list
implement insert and delete seperately check lru capacity lastly and delete from linked list and dict
'''


class Node:
    def __init__(self, key=0, val=0, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt

class LRUCache:

    def __init__(self, capacity):
        # Store all data
        self.cache = {}
        self.capacity = capacity
        # Track LSU, right for most recent used and left for least recent used
        self.left = Node()
        self.right = Node()
        self.left.nxt = self.right
        self.right.prev = self.left
    
    def insert(self,node):
        prev = self.right.prev
        nxt = self.right
        node.prev = prev
        node.nxt = nxt
        prev.nxt = node
        nxt.prev = node

    def delete(self,node):
        prev = node.prev
        nxt = node.nxt
        prev.nxt = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.delete(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        
        if key not in self.cache:
            newNode = Node(key,value)
            self.cache[key] = newNode
            self.insert(newNode)
        else:
            newNode = Node(key,value)
            self.delete(self.cache[key])
            self.cache[key] = newNode
            self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            key = self.left.nxt.key
            self.delete(self.left.nxt)
            del self.cache[key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)