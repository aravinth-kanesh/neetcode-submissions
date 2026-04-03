# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # inorder traversal of a valid BST gives us sorted order

        self.order = []

        # left, root, right
        def inorder(node):
            if not node:
                return

            inorder(node.left)
            self.order.append(node.val)
            inorder(node.right)

        # run inorder() on root
        inorder(root)

        n = len(self.order)

        if n == 1:
            return True

        for i in range(1, n):
            # not in sorted order
            if self.order[i] <= self.order[i - 1]:
                return False

        return True