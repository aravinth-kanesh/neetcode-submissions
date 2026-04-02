# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # use range tracking
        # anything below or equal to min_val is invalid
        # anything above or equal to max_val is invalid
        def validate(node, min_val, max_val):
            # base case
            if not node:
                return True

            if node.val <= min_val or node.val >= max_val:
                return False

            # validate left and right subtrees
            return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)

        return validate(root, float('-inf'), float('inf'))