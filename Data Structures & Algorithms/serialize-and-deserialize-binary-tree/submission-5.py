# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        res = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if not node:
                res.append("null|")
                continue

            res.append(f"{node.val}|")

            queue.append(node.left)
            queue.append(node.right)

        print("".join(res))
        return "".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None

        vals = data.split("|")
        print(vals)

        root = TreeNode(int(vals[0]))
        queue = deque([root])

        i = 1

        while queue:
            node = queue.popleft()

            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1

            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1

        return root

