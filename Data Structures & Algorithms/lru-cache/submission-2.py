# doubly linked list node to maintain used order
class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None 

class LRUCache:
    def __init__(self, capacity: int):
        # initialise capacity
        self.cap = capacity

        # initialise the cache - maps key to Node
        self.cache = {}

        # initialise the doubly linked list

        # initialise both ends to track used order
        # keys never stored in cache, so both can be set to same val
        self.lru = Node(0, 0)
        self.mru = Node(0, 0)

        # connect the two ends
        self.lru.next = self.mru
        self.mru.prev = self.lru

    def get(self, key: int) -> int:
        if key in self.cache:
            # rememeber the cache stores the Node object, not the val
            node = self.cache[key]
            value = node.val

            # remove it from its place in the dll
            self.remove(node)

            # move it to the mru end
            self.insert(node)

            # return the value
            return value
        
        # key does not exist in the cache
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            
            # update the value
            node.val = value

            self.remove(node)
            self.insert(node)
        # key is not in the cache
        else:
            # place it in the cache first
            node = Node(key, value)
            self.cache[key] = node

            # insert it to the mru side
            self.insert(node)

            # check if capacity exceeded
            if len(self.cache) > self.cap:
                node_to_remove = self.lru.next
                self.remove(node_to_remove)
                del self.cache[node_to_remove.key]

    def insert(self, node):
        prev_node = self.mru.prev

        prev_node.next = node
        node.prev = prev_node

        node.next = self.mru
        self.mru.prev = node

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node
        
