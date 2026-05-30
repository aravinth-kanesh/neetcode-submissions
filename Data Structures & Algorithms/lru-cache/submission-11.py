# dll node
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key -> dll node

        # both ends of the dll
        self.lru = Node(0, 0)
        self.mru = Node(0, 0)

        # connect both ends
        self.lru.next = self.mru
        self.mru.prev = self.lru

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            # remove it from the dll and move it to the mru end
            self.remove(node)
            self.insert(node)

            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)

        # create the new dll node and add it to the cache
        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node

        # check if capacity exceeded
        if len(self.cache) > self.cap:
            lru = self.lru.next
            self.remove(lru)

            # remove the hashmap entry
            del self.cache[lru.key]
    
    # remove a node from the dll
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    # insert a node at the mru end
    def insert(self, node):
        prev = self.mru.prev
        prev.next = node
        node.prev = prev
        node.next = self.mru
        self.mru.prev = node 
        
