# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(l_node, r_node):
            if not l_node and not r_node:
                return True
            
            if not l_node or not r_node:
                return False
            
            cur_check = l_node.val == r_node.val
            left_check = dfs(l_node.left, r_node.right)
            right_check = dfs(l_node.right, r_node.left)

            return cur_check and left_check and right_check
        
        return dfs(root.left, root.right)
            
