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

        nodes = {}

        cur = head
        while cur:
            nodes[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            nodes[cur].next = nodes.get(cur.next)
            nodes[cur].random = nodes.get(cur.random)
            cur = cur.next

        return nodes[head]