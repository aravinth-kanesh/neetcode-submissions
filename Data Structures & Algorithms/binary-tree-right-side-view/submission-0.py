# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # key insight - use BFS to perform level-order traversal
        # and add right-most node of each level to tree
        result = []

        if not root:
            return result

        queue = deque([root])

        while queue:
            # nodes in current level
            level = []
            
            # process level-by-level
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                # next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # add "final" node to the result
            result.append(level[-1])

        return result