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
            if not node:
                return

            # first time visiting this level
            if depth == len(result):
                result.append(node.val)
            
            # explore right first
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return result