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

        clones = {node: Node(node.val)}

        queue = deque([node])

        # save original reference
        start = node

        while queue:
            node = queue.popleft()

            for neighbor in node.neighbors:
                if neighbor not in clones:
                    # create a clone if doesn't exist
                    clones[neighbor] = Node(neighbor.val)

                    # add it to the queue
                    queue.append(neighbor)

                # add it to the neighbors list
                clones[node].neighbors.append(clones[neighbor])

        return clones[start]