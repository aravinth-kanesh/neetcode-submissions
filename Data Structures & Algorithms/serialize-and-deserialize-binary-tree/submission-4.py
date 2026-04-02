# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []

        if not root:
            return ""

        def preorder(node):
            if not node:
                result.append("null")
                return
            else:
                result.append(str(node.val))
                preorder(node.left)
                preorder(node.right)

        preorder(root)
        return ",".join(result)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        nodes = data.split(",")
        self.index = 0

        def dfs():
            if nodes[self.index] == "null":
                self.index += 1
                return
            
            node = TreeNode(int(nodes[self.index]))

            self.index += 1
            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()
