# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, l_d=p, r_d=q):
            if not node:
                return None
            
            if l_d.val < node.val and r_d.val < node.val:
                return dfs(node.left)
            elif l_d.val > node.val and r_d.val > node.val:
                return dfs(node.right)
            else:
                return node
        
        return dfs(root)