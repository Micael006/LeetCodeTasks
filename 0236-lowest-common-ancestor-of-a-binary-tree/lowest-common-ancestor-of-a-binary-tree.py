# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, left=False, right=False, l_d=p, r_d=q):
            if not node:
                return left, right, None
            
            l1, r1, l_a1 = dfs(node.left, left, right)
            l2, r2, l_a2 = dfs(node.right, left, right)

            if node.val == l_d.val:
                left = True
            if node.val == r_d.val:
                right = True

            left = left or l1 or l2
            right = right or r1 or r2

            if l1 and r1:
                return l1, r1, l_a1
            elif l2 and r2:
                return l2, r2, l_a2
            elif left and right:
                return left, right, node
            return left, right, None
        
        return dfs(root)[-1]