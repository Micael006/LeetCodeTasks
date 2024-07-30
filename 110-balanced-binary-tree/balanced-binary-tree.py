# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.check = True
        def dfs(node):
            if not node:
                return 0
            
            l_height = dfs(node.left)
            r_height = dfs(node.right)

            if abs(r_height - l_height) > 1:
                self.check = False

            return max(l_height, r_height) + 1

        dfs(root)
        return self.check