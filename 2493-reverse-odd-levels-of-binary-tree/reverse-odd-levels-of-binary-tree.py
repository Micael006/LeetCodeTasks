# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        q.append([root, 0])
        result = []
        while q:
            cur, lvl = q.popleft()
            if len(result) < lvl + 1:
                result.append([])
            result[lvl].append(cur)
            if cur.left:
                q.append([cur.left, lvl+1])
                q.append([cur.right, lvl+1])
        
        for i in range(1, len(result), 2):
            helper = [x.val for x in result[i]]
            for j in range(len(result[i])):
                result[i][j].val = helper[-j - 1]
        
        return root
        