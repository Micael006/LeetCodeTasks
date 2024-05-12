# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(node_left, node_right) -> bool:
            if node_left is None and node_right is None:
                return True
            elif node_left is None or node_right is None:
                return False
            if node_left.val != node_right.val:
                return False
            return dfs(node_left.left, node_right.right) and dfs(node_left.right, node_right.left)

        return dfs(root.left, root.right)            
            
