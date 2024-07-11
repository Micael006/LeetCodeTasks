# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []

        if not root:
            return []
        
        q = deque()
        q.append([root, 0])

        while q:
            node, level = q.popleft()

            if len(levels) == level:
                levels.append([])
            
            levels[level].append(node.val)

            if node.left:
                q.append([node.left, level + 1])
            if node.right:
                q.append([node.right, level + 1])
            
        for i in range(1, len(levels), 2):
            levels[i] = levels[i][::-1]
        
        return levels