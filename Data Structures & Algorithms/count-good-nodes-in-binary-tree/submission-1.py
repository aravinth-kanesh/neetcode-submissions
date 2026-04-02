# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # binary tree - at most 2 child nodes: a left and a right

        self.good = 0

        if not root:
            return self.good

        path = []

        def dfs(node):
            # don't recurse further
            if not node:
                return

            # root node or no nodes with a value greater 
            # than the current node
            if not path or node.val >= max(path):
                self.good += 1

            path.append(node.val)

            dfs(node.left)
            dfs(node.right)

            path.pop()

        dfs(root)
        return self.good
