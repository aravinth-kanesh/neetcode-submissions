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
        copies = {} # maps old node -> new node

        def dfs(node):
            # null - prevent infinite recursion
            if not node:
                return

            # node already copied
            if node in copies:
                return copies[node]

            # node not copied yet
            copy = Node(node.val)
            copies[node] = copy

            # copy next and random nodes recursively
            copy.next = dfs(node.next)
            copy.random = dfs(node.random)

            return copy

        return dfs(head)