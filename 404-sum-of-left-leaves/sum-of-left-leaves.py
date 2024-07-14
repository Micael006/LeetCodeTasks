# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        cur_sum = 0
        if root.left:
            if (not root.left.left) and (not root.left.right):
                cur_sum += root.left.val
            cur_sum += self.sumOfLeftLeaves(root.left)
        if root.right:
            cur_sum += self.sumOfLeftLeaves(root.right)
        
        return cur_sum