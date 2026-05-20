# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        # calculate height of node recursively
        def dfs(node):
            # base case when no node
            if not node:
                return 0

            # calculate heights of left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # update diameter
            # diameter is max(left subtree height + right subtree)
            self.diameter = max(self.diameter, left_height + right_height)

            # return height of node using known calculation
            return 1 + max(left_height, right_height)

        dfs(root)
        return self.diameter