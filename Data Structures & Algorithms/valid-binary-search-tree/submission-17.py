# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # recursion problem - can use dfs
        def dfs(node, min_val, max_val):
            # stop infinite recursion
            if not node:
                return True

            # must be within the valid range
            if not (min_val < node.val < max_val):
                return False

            # recurse for subtrees
            # for left subtree, max_val is now node.val
            # for right subtee, min_val is now node.val
            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

        # start recursion at the root
        return dfs(root, float('-inf'), float('inf'))

            