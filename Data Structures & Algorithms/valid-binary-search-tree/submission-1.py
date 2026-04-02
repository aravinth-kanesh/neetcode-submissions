# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Key insight - in-order traversal of a valid BST would be
        # sorted
        def inorder(root):
            # left --> root --> right
            result = []

            if not root:
                return result

            result += inorder(root.left)
            result.append(root.val)
            result += inorder(root.right)

            return result
        
        inorder = inorder(root)

        if not inorder:
            return True

        for i in range(1, len(inorder)):
            if inorder[i] <= inorder[i - 1]:
                return False

        return True 
