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

        # time - O(n), where n is the number of nodes in the tree
        # space - O(h), where h is the height of the tree. In the worst
        # case, this is O(n), but in the best case it is O(log(n)), when
        # it is a balanced tree