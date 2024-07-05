# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        min_dist = -1
        max_dist = -1
        cur_counter = 0
        cur_max_counter = 0
        found_extremum = False
        last = head
        cur = head.next
        while cur is not None and cur.next is not None:
            if (last.val < cur.val and cur.next.val < cur.val) or (last.val > cur.val and cur.next.val > cur.val):
                if found_extremum:
                    if min_dist == -1 or min_dist > cur_counter:
                        min_dist = cur_counter
                    max_dist = cur_max_counter
                found_extremum = True
                cur_counter = 0

            if found_extremum:
                cur_counter += 1
                cur_max_counter += 1

            last = last.next
            cur = last.next
        
        return [min_dist, max_dist]