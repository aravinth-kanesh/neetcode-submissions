# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            # p and q in the left subtree, so is LCA
            if p.val < root.val and q.val < root.val:
                root = root.left
            # p and q in the right subtree, so is LCA
            elif p.val > root.val and q.val > root.val:
                root = root.right
            # p and q in different subtrees, LCA is current node
            else:
                return root

        # time - O(h), where h is the height of the tree. O(logn) for a
        # balancd BST, O(n) worst case case (when tree is essentially
        # a linked list)
        # space - O(1), since no extra space used