# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque()
        q.append([root, 0])

        levels = []
        while q:
            node, lvl = q.popleft()
            if len(levels) < lvl + 1:
                levels.append(-2**32)
            if levels[lvl] < node.val:
                levels[lvl] = node.val
            if node.left:
                q.append([node.left, lvl + 1])
            if node.right:
                q.append([node.right, lvl + 1])
        
        return levels