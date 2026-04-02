# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0

        if not root:
            return self.good

        path = []

        def dfs(node):
            if not node:
                return

            if not path or node.val >= max(path):
                self.good += 1

            path.append(node.val)

            dfs(node.left)
            dfs(node.right)

            path.pop()

        dfs(root)
        return self.good