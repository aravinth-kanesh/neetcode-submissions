# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if not root:
            return result

        queue = deque([root])

        while queue:
            # store nodes in current level
            same_level = []

            # process level by level
            for _ in range(len(queue)):
                node = queue.popleft()

                # only append the value
                same_level.append(node.val)

                # add left and right to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # level has now been processed, add array to result
            result.append(same_level)

        return result

            