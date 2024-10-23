# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def addCousinSum(node):
            if not node:
                return
            helper = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
            
            if node.left:
                node.left.val = helper
                addCousinSum(node.left)
            if node.right:
                node.right.val = helper
                addCousinSum(node.right)
        
        q = deque()
        q.append([root, 0])
        level_sums = dict()

        while q:
            cur, level = q.popleft()
            level_sums[level] = level_sums.get(level, 0) + cur.val

            if cur.left:
                q.append([cur.left, level + 1])
            if cur.right:
                q.append([cur.right, level + 1])

        addCousinSum(root)

        q = deque()
        q.append([root, 0])

        while q:
            cur, level = q.popleft()
            cur.val = level_sums[level] - cur.val

            if cur.left:
                q.append([cur.left, level + 1])
            if cur.right:
                q.append([cur.right, level + 1])
        
        return root
