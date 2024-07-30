# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def tree_to_string(node):
            if not node:
                return ""
            
            left_tree = tree_to_string(node.left)
            right_tree = tree_to_string(node.right)

            return str(node.val) + "_" + left_tree + "_" + right_tree
        
        def dfs(node, table=dict()):
            if not node:
                return table

            cur_tree = tree_to_string(node)
            table[cur_tree] = table.get(cur_tree, []) + [node]

            table = dfs(node.left, table)
            table = dfs(node.right, table)

            return table
        
        all_subtrees = dfs(root)
        answer = []
        for key in all_subtrees:
            if len(all_subtrees[key]) > 1:
                answer.append(all_subtrees[key][0])
        
        return answer