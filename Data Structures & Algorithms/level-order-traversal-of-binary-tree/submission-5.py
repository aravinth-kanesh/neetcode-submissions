# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        # can have 0 nodes in the tree as an edge case
        if not root:
            return result

        # bfs implementation
        queue = deque([root])

        while queue:
            # store the nodes at the current level
            cur_level = []

            for _ in range(len(queue)):
                node = queue.popleft()

                # append the node to the current level
                cur_level.append(node.val)

                # add the left and right nodes to the queue (if they
                # are not None)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # add the level to the results list
            result.append(cur_level)

        return result
