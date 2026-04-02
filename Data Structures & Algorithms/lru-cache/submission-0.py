# tbh, I feel like this can be done with a deque, but I haven't
# thought about the logistics yet.

# doubly linked list node
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        # O(1) time complexity tells me that I should use a hash map
        # this would've been my go-to anyways
        self.cap = capacity
        # hashmap maps key --> node
        self.cache = {}
        # use a linked list to store cache items from LRU to MRU
        # create dummy nodes for O(1) access at the ends
        self.lru, self.mru = Node(0, 0), Node(0, 0)
        self.lru.next = self.mru
        self.mru.prev = self.lru

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val
        
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def insert(self, node):
        prev = self.mru.prev
        next = self.mru
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.lru.next
            self.remove(lru)
            del self.cache[lru.key]
