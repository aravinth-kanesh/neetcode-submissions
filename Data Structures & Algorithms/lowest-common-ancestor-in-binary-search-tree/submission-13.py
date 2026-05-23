# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Three cases:
        # 1. p and q are in either subtree
        # 2. p is the LCA
        # 3. q is the LCA

        # we can use the BST property to our favour
        # keep repeating whilst there are nodes to look at

        while root:    
            # LCA is in the left subtree
            if p.val < root.val and q.val < root.val:
                root = root.left
            # LCA is in the right subtree
            elif p.val > root.val and q.val > root.val:
                root = root.right
            # found LCA
            else:
                return root