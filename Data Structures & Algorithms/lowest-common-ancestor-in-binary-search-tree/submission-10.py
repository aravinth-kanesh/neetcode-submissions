# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # helper function
        def find_lca(node):
            # current node is the lca - p and q are on either side or is p or q
            if (p.val < node.val < q.val) or (q.val < node.val < p.val) or node.val == p.val or node.val == q.val:
                return node

            # lca is in the left subtree
            if node.val > p.val and node.val > q.val:
                return find_lca(node.left)
            # in the right subtee
            elif node.val < p.val and node.val < q.val:
                return find_lca(node.right)

        return find_lca(root)