# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        if not root:
            return result

        def dfs(node, depth):
            # prevent infinite recursion
            if not node:
                return

            # visiting this level for the first time
            if len(result) == depth:
                result.append(node.val)

            # look for right node first
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return result