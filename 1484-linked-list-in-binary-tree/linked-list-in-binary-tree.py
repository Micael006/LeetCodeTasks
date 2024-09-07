# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        subtrees = [[]]
        def dfs(node, index):
            if not node:
                return 

            subtrees[index].append(node.val)
            if node.left and node.right:
                subtrees.append(subtrees[index][:])
                dfs(node.right, len(subtrees) - 1)
                dfs(node.left, index)
            elif node.left:
                dfs(node.left, index)
            elif node.right:
                dfs(node.right, index) 
        
        dfs(root, 0)
        print(*subtrees, sep='\n')

        for subtree in subtrees:
            if head.val not in subtree:
                continue
            cur = subtree[subtree.index(head.val):]

            while head.val in cur:
                helper = head
                cur_index = 0
                while helper and cur_index < len(cur):
                    if helper.val != cur[cur_index]:
                        break
                    helper = helper.next
                    cur_index += 1
                if not helper:
                    return True
                if head.val not in cur[1:]:
                    break
                new_pos = cur[1:].index(head.val) + 1
                cur = cur[new_pos:]

        return False
