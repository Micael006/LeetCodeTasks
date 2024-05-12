# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, min_val, max_val):
            if node is None:
                return True
            if node.val <= min_val or node.val >= max_val:
                return False
            if node.left:
                if node.left.val >= node.val:
                    return False
            if node.right:
                if node.right.val <= node.val:
                    return False
            
            return dfs(node.left, min_val, min(node.val, max_val)) and dfs(node.right, max(node.val, min_val), max_val)
  
        return dfs(root, -2**32, 2**32)
