"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # edge case - return None if no input node
        if not node:
            return None

        clones = {}

        # function to clone the current node and subsequently all of
        # the other nodes
        def dfs(node):
            if node in clones:
                return clones[node]

            clone = Node(node.val)
            clones[node] = clone

            # complete the graph structure by cloning all neighbours
            for neighbour in node.neighbors:
                clone.neighbors.append(dfs(neighbour))

            return clone

        return dfs(node)