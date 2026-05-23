# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # need to recursively check left and right subtrees
        # the lowest node that has p and q as descendants (including
        # itself is the LCA)

        # case 1 - current node is p or q - so lca is current node
        if not root or root is p or root is q:
            return root

        # each call only returns something if it found p or q
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # p and q found in either subtree - lca is current node
        if left and right:
            return root

        # either one of p or q found or None is returned
        return left or right