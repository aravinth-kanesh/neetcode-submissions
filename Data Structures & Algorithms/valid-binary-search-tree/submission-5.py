# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # use range tracking - check if each node's value is within
        # its allowed range
        def validate(node, min_val, max_val):
            # base case
            if not node:
                return True

            if node.val <= min_val or node.val >= max_val:
                return False

            # left subtree must be < node.val
            # right subtree must be > node.val
            return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)

        return validate(root, float('-inf'), float('inf'))