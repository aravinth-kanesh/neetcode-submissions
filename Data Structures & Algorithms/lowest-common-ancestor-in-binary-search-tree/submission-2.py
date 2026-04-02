# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # all node values are unique - no possibility of getting multiple
        # solutions. This means that p and q must be different - simplifies
        # edge cases.

        # another thing to mention is that a node can be the LCA of itself,
        # so it may be the case that p or q is the LCA

        # key insight with a binary search tree - if p and q > node,
        # then the LCA is in the right subtree. If p and q < node,
        # then the LCA is the left subtree. Otherwise, the current node
        # is the lCA

        # iterative approach
        # until we hit a None
        while root:
            # case 1 - p and q > node
            if p.val > root.val and q.val > root.val:
                # LCA is in the right subtree
                root = root.right

            # case 2 - p and q < node
            elif p.val < root.val and q.val < root.val:
                # LCA is in the left subtree
                root = root.left

            # case 3 - one of p and q is in the left subtree,
            # and the other is in the right subtree
            else:
                return root

        # assuming that there is also a valid answer, so not outer return
        # statement

            