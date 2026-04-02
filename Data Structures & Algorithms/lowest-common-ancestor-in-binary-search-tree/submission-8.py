# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # return the LCA of p and q
        def dfs(node):
            if not node:
                return

            val = node.val

            # scenario 1, both p and q are in the left subtree
            if p.val < val and q.val < val:
                return dfs(node.left)
            # scenario 2, both p and q are in the right subtree
            elif p.val > val and q.val > val:
                return dfs(node.right)
            # scenario 3, LCA has been found
            else:
                return node

        return dfs(root)