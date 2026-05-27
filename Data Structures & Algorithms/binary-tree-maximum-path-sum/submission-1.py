# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = root.val

        # return max path sum without split
        def dfs(node):
            if not node:
                return 0
            
            left_max = dfs(node.left)
            right_max = dfs(node.right)

            # max path sum shouldn't be "worse"
            left_max = max(0, left_max)
            right_max = max(0, right_max)

            # compute max path sum with split - if this node was split
            self.max_sum = max(self.max_sum, node.val + left_max + right_max)

            # return max path sum without split
            return node.val + max(left_max, right_max)

        dfs(root)
        return self.max_sum