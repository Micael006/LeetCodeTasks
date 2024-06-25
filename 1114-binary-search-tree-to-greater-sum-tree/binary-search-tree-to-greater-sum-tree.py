# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node, val):
            if node is None:
                return val
            
            right_val = dfs(node.right, val)
            node.val += right_val
            left_val = dfs(node.left, node.val)
            return max(node.val, left_val)
        
        dfs(root, 0)
        return root