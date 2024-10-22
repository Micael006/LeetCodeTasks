# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque()
        q.append([root, 1])
        level_sums = []

        while q:
            cur, level = q.popleft()
            if len(level_sums) < level:
                level_sums.append(0)
            level_sums[level - 1] += cur.val

            if cur.left:
                q.append([cur.left, level + 1])
            if cur.right:
                q.append([cur.right, level + 1])
        
        if len(level_sums) < k:
            return -1
        return sorted(level_sums)[-k]