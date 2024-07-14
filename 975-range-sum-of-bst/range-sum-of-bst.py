# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        cur_sum = 0
        if low <= root.val <= high:
            cur_sum += root.val
        
        cur_sum += self.rangeSumBST(root.left, low, high)
        cur_sum += self.rangeSumBST(root.right, low, high)

        return cur_sum