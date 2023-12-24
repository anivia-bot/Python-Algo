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
'''


class Node: 
    # This algo runs in O(1) time and take up O(N) space
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right
        node.prev = prev
        node.next = nxt
        prev.next = node
        nxt.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
        else:
            self.remove(self.cache[key])
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)