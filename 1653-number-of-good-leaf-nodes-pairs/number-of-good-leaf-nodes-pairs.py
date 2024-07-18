# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.paths = []
        self.cur_path = []

        def dfs(node):
            if not node:
                return None
            
            if not (node.left or node.right):
                self.paths.append(''.join(self.cur_path))
                return None
            
            self.cur_path.append('L')
            dfs(node.left)
            self.cur_path.pop()

            self.cur_path.append('R')
            dfs(node.right)
            self.cur_path.pop()
        
        dfs(root)
        
        count = 0

        for i in range(len(self.paths)):
            path1 = self.paths[i]
            for j in range(i + 1, len(self.paths)):
                path2 = self.paths[j]
                l1 = 0
                l2 = 0
                while l1 < len(path1) and l2 < len(path2):
                    if path1[l1] != path2[l2]:
                        break
                    l1 += 1
                    l2 += 1
                
                if len(path1) + len(path2) - l1 - l2 <= distance:
                    count += 1
        
        return count