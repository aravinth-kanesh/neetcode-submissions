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

        # maps old node --> cloned node
        clones = {}

        def dfs(node):
            # check if it has already been cloned
            if node in clones:
                return clones[node]

            # clone the node and add the mapping to the hashmap
            clone = Node(node.val)
            clones[node] = clone

            # clone all of the node's neighbours
            for neighbour in node.neighbors:
                clone.neighbors.append(dfs(neighbour))

            return clone

        # outer "loop"
        return dfs(node)



        