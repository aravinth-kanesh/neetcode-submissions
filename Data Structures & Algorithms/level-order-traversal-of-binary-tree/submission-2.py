# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # level order traversal - BFS
        # nested list - each level is contained within an array
        # output contains the value - append values, not actual nodes
        result = []

        # edge case - no tree
        if not root:
            return result

        # deque for bfs
        queue = deque([root])

        while queue:
            # list to store the nodes at the current level
            same_level = []

            # process level-by-level
            for _ in range(len(queue)):
                node = queue.popleft()
                same_level.append(node.val)

                # add left and right nodes to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # add current level to the final nested list
            result.append(same_level)

        return result