class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = []

        def inorder(node):
            if not node:
                return
                
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)

        for i in range(1, len(result)):
            if result[i] <= result[i - 1]:  # strict inequality
                return False

        return True