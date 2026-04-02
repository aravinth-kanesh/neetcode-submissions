# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # input: root of a tree
        # output: a single string
        result = []
        
        # edge case - no tree
        if not root:
            return ""

        """multiple approaches - 1. perform an preorder traversal of the
        tree, ensuring to represent leaf nodes correctly with "null" left
        and right nodes"""
        
        # preorder traversal helper using dfs
        # why preorder
        def preorder(node):
            # root -> left -> right
            # function has no return type

            # base case
            if not node:
                # represents null
                result.append("N")
                return

            # add node to result
            result.append(str(node.val))

            # process left and right nodes in that order
            preorder(node.left)
            preorder(node.right)

        # serialise the whole tree
        preorder(root)

        # convert to a string
        return ",".join(result)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # edge case
        if not data:
            return None

        # example 'data': "1,2,N,N,3,4,N,N,5,N,N"
        # need to convert string back to a tree

        # make the data easy to parse
        nodes = data.split(",") # example nodes - [1, 2, N, N, 3, 4... ,N]
        # be careful - numbers in nodes will be strings/chars

        # "global" i
        self.index = 0

        # dfs to build the tree
        # returns tree node
        def dfs():
            if nodes[self.index] == "N":
                self.index += 1
                # do nothing (except increment i) - do not create a node
                return

            # nodes[i] is a valid node
            node = TreeNode(int(nodes[self.index]))

            # recursively build left and right subtrees
            self.index += 1
            node.left = dfs()
            node.right = dfs()

            # return TreeNode
            return node

        return dfs()
        