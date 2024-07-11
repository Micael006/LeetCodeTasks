# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, cur_min, cur_max):
            if not node:
                return True
            
            cur_tree = cur_min < node.val < cur_max

            left_tree = True
            if node.left:
                left_tree = dfs(node.left, cur_min, node.val)
            
            right_tree = True
            if node.right:
                right_tree = dfs(node.right, node.val, cur_max)

            return cur_tree and left_tree and right_tree
        
        return dfs(root, -2**32, 2**32)