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
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                if i == level_size - 1:
                    result.append(node.val)
                
                # next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result