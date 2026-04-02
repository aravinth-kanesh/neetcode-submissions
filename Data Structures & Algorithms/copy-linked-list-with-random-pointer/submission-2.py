"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        mapping = {}

        # create new nodes
        cur = head
        while cur:
            mapping[cur] = Node(cur.val)
            cur = cur.next

        # assign pointers
        cur = head
        while cur:
            if cur.next:
                mapping[cur].next = mapping[cur.next]

            if cur.random:
                mapping[cur].random = mapping[cur.random]

            cur = cur.next

        return mapping[head]

        
