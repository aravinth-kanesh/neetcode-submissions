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

            # add to result if first time visiting this depth
            if len(result) == depth:
                result.append(node.val)

            # check the right node first
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        # start at the root
        dfs(root, 0)
        return result