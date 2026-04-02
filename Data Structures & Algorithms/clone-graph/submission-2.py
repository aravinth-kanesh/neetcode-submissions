"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_map = {}

        def clone_dfs(node):
            if node in node_map:
                return node_map[node]

            copy = Node(node.val)
            node_map[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(clone_dfs(nei))

            return copy

        return clone_dfs(node) if node else None