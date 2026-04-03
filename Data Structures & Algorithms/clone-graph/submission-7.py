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
            
        # use a hashmap to map original nodes to their clones
        clones = {}

        # helper dfs function
        # role of this function is to clone the node and all of its 
        # neighbours
        def dfs(node):
            if node in clones:
                return clones[node]

            # clone the node and add it to the hashmap
            clone = Node(node.val)
            clones[node] = clone

            # clone all the neighbours and add it as neighbours to the
            # cloned node
            for neighbour in node.neighbors:
                clone.neighbors.append(dfs(neighbour))

            # return the cloned node object with all cloned neighbours
            return clone

        return dfs(node)