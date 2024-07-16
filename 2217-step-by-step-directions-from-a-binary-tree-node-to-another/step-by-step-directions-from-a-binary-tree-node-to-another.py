# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.cur_path = []
        def path_to_node(node, search_val):
            if not node:
                return None

            if node.val == search_val:
                return self.cur_path
            
            self.cur_path.append('L')
            left_path = path_to_node(node.left, search_val)
            if left_path is not None:
                return left_path
            self.cur_path.pop()
            

            self.cur_path.append('R')
            right_path = path_to_node(node.right, search_val)
            if right_path is not None:
                return right_path
            self.cur_path.pop()

            return None

            
        
        start_val_path = ''.join(path_to_node(root, startValue))
        self.cur_path = []
        end_val_path = ''.join(path_to_node(root, destValue))

        l = 0
        while l < len(start_val_path) and l < len(end_val_path):
            if start_val_path[l] != end_val_path[l]:
                break
            l += 1
        
        start_val_path = 'U' * len(start_val_path)
        
        return start_val_path[l:] + end_val_path[l:]