# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        def dfs(node, cur_str):
            cur_str += ' '
            if node.left:
                cur_str += str(node.left.val)
                cur_str = dfs(node.left, cur_str)
            else:
                cur_str += "None"
            
            cur_str += ' '
            if node.right:
                cur_str += str(node.right.val)
                cur_str = dfs(node.right, cur_str)
            else:
                cur_str += "None"
            
            return cur_str
        
        if not root:
            return "None"
        return f"{root.val}" + dfs(root, "")

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if data == "None":
            return None
        
        nodes = data.split()

        def dfs(node, arr, cur_idx):
            if arr[cur_idx] == "None":
                node.left = None
                cur_idx += 1
            else:
                node.left = TreeNode(int(arr[cur_idx]))
                cur_idx += 1
                node.left, cur_idx = dfs(node.left, arr, cur_idx)
            
            if arr[cur_idx] == "None":
                node.right = None
                cur_idx += 1
            else:
                node.right = TreeNode(int(arr[cur_idx]))
                cur_idx += 1
                node.right, cur_idx = dfs(node.right, arr, cur_idx)

            return node, cur_idx

        tree = TreeNode(int(nodes[0]))
        return dfs(tree, nodes, 1)[0]

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans