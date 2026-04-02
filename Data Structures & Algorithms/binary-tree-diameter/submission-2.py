# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        if not root:
            return self.diameter

        # key insight - longest path through a node goes from
        # deepest node in left subtree -> node -> deepest node in right
        # subtree

        # dfs implementation
        # why: need to calculate longest path through EVERY node

        # calculates height recursively
        def dfs(node):
            if not node:
                return 0

            # calculate left and right heights
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # update diameter
            self.diameter = max(self.diameter, left_height + right_height)

            # return height for parent node
            # 1 + since the height includes itself
            return 1 + max(left_height, right_height)

        dfs(root)
        return self.diameter