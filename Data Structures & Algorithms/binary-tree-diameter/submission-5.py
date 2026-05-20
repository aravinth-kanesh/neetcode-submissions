# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        # calculates height recursively
        def dfs(node):
            # base case
            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # diameter is height of left subtree + right one
            self.diameter = max(self.diameter, left_height + right_height)

            # return the height of the node
            return 1 + max(left_height, right_height)

        dfs(root)
        return self.diameter

        