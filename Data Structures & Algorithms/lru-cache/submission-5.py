class Node:
    def __init__(self):
        self.key = None
        self.val = 0
        self.prev = None
        self.next = None

# use a doubly linked list to store lru -> mru

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        self.cache = {} # maps key -> dll node
        
        self.lru, self.mru = Node(), Node()
        self.lru.next = self.mru
        self.mru.prev = self.lru
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val

        # key not in the cache
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # remove it from the linked list and add it back to
            # the mru side
            node = self.cache[key]
            self.remove(node)

            # update the value of the node
            node.val = value
            self.insert(node)

            return

        # key is not in the cache

        # first create the linked list node
        node = Node()
        node.key, node.val = key, value

        # add it to the linked list at the mru side
        self.insert(node)

        # add it to the cache
        self.cache[key] = node

        # perform the capacity check
        if len(self.cache) > self.capacity:
            self.remove(self.lru.next)

    def remove(self, node):
        prev_node, next_node = node.prev, node.next

        # sever the linked list connection
        prev_node.next, next_node.prev = next_node, prev_node

        # remove the cache entry
        del self.cache[node.key]

    def insert(self, node):
        prev_node, next_node = self.mru.prev, self.mru

        # insert it to the end of the list (mru side)
        prev_node.next, node.prev = node, prev_node
        node.next, next_node.prev = next_node, node

        self.cache[node.key] = node
        
