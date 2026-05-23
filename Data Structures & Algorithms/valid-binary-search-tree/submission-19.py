# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # inherently a recursive problem, so we can use dfs
        # need to recursively check BST validity
        # every node has a min val and max_val, must be within
        # that range
        def dfs(node, min_val, max_val):
            # base case - no node
            if not node:
                # automatically satisfied
                return True

            # range check
            if not(min_val < node.val < max_val):
                return False

            # recursively check left and right subtrees
            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

        return dfs(root, float('-inf'), float('inf'))