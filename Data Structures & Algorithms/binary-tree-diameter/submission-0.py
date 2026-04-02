# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # key insight - longest path through a node = left height
        # + right height

        # make diameter a "global" variable
        diameter = [0]

        if not root:
            return diameter[0]

        # return 1 + max(left_height, right_height)
        def dfs(node):
            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            diameter[0] = max(diameter[0], left_height + right_height)

            return 1 + max(left_height, right_height)

        dfs(root)
        return diameter[0]