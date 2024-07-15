# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        parent_to_child = dict()
        child_to_parent = dict()

        for desc in descriptions:
            if desc[0] not in parent_to_child:
                parent_to_child[desc[0]] = [None, None]
            
            if desc[0] not in child_to_parent:
                child_to_parent[desc[0]] = None

            child_to_parent[desc[1]] = desc[0]

            if desc[2]:
                parent_to_child[desc[0]][0] = desc[1]
            else:
                parent_to_child[desc[0]][1] = desc[1]
        
        root = -1
        for key in child_to_parent:
            if child_to_parent[key] is None:
                root = key
                break
        
        root = TreeNode(root)
        q = deque()
        q.append(root)

        while q:
            cur_node = q.popleft()
            if cur_node.val not in parent_to_child:
                continue
            
            if parent_to_child[cur_node.val][0] is not None:
                cur_node.left = TreeNode(parent_to_child[cur_node.val][0])
                q.append(cur_node.left)
            
            if parent_to_child[cur_node.val][1] is not None:
                cur_node.right = TreeNode(parent_to_child[cur_node.val][1])
                q.append(cur_node.right)
        
        return root

            
        