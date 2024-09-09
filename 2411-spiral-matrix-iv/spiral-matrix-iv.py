# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for j in range(n)] for i in range(m)]
        cur_pos = [0, -1]
        m -= 1
        directions = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]
        ]
        cur_dir = 0
        cur = head
        while cur:
            for _ in range(n):
                if not cur:
                    return matrix
                cur_pos[0] += directions[cur_dir][0]
                cur_pos[1] += directions[cur_dir][1]
                matrix[cur_pos[0]][cur_pos[1]] = cur.val
                cur = cur.next
            n -= 1
            cur_dir = (cur_dir + 1) % len(directions)
            for _ in range(m):
                if not cur:
                    return matrix
                cur_pos[0] += directions[cur_dir][0]
                cur_pos[1] += directions[cur_dir][1]
                matrix[cur_pos[0]][cur_pos[1]] = cur.val
                cur = cur.next
            m -= 1
            cur_dir = (cur_dir + 1) % len(directions)
        
        return matrix


            