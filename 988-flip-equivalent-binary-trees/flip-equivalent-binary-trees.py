# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            elif (not node1 and node2) or (node1 and not node2):
                return False
            elif node1.val != node2.val:
                return False
            elif (node1.left is not None) + (node1.right is not None) - (node2.left is not None) - (node2.right is not None) != 0:
                return False
            
            needs_swap = False

            if node1.left and node2.left:
                if node1.left.val != node2.left.val:
                    needs_swap = True
            elif node1.right and node2.right:
                if node1.right.val != node2.right.val:
                    needs_swap = True
            elif (node1.left and node2.right) or (node1.right and node2.left):
                needs_swap = True
            
            if needs_swap:
                temp = node1.left
                node1.left = node1.right
                node1.right = temp
            
            left, right = True, True
            if node1.left:
                left = dfs(node1.left, node2.left)
            if node1.right:
                right = dfs(node1.right, node2.right)

            return left and right
        
        return dfs(root1, root2)