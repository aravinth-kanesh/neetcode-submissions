# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        # edge case
        if not root:
            return result

        queue = deque([root])

        # bfs implementation - level-order traversal
        while queue:
            # store nodes in the current level
            level = []

            # process level-by-level
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                # next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # add current level to result
            result.append(level)

        return result 