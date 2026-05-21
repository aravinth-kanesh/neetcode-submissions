# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # kth smallest value - keep a max heap of k smallest values
        # heap[0] will give kth smallest value
        max_heap = []
        heapq.heapify(max_heap)

        def dfs(node):
            # prevent infinite recursion
            if not node:
                return

            if len(max_heap) < k:
                heapq.heappush(max_heap, -node.val)
            # heap is full
            elif node.val < -max_heap[0]:
                heapq.heapreplace(max_heap, -node.val)

            # recurse on left and right nodes
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return -max_heap[0]