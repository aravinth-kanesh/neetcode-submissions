# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = root.val

        # return the max path sum WITHOUT split (root + max(left, right))
        def dfs(node):
            if not node:
                return 0

            left_max = dfs(node.left)
            right_max = dfs(node.right)

            # negative subtree path sum affects answer
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            # max path sum WITH current node as split point (left + root + right)
            self.max_sum = max(self.max_sum, node.val + left_max + right_max)

            return node.val + max(left_max, right_max)

        dfs(root)
        return self.max_sum