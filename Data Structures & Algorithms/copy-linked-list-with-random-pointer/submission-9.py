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
        copies = {}

        # return copied node
        def dfs(node):
            if not node:
                return None

            # node already copied
            if node in copies:
                return copies[node]

            # make a copy
            copy = Node(node.val)
            copies[node] = copy

            copy.next = dfs(node.next)
            copy.random = dfs(node.random)

            return copy

        return dfs(head)