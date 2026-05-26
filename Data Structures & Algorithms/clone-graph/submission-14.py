"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clones = {} # old node -> new node

        # use dfs to explore all nodes (and return the cloned node)
        def dfs(node):
            if not node:
                return None

            # do not copy again
            if node in clones:
                return clones[node]

            # make the copy
            copy = Node(node.val) # value of the node
            clones[node] = copy

            # recursively clone all neighbours
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            # return cloned node
            return copy

        return dfs(node)
                