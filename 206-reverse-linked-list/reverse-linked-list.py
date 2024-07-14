# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        parent = None
        remains = None
        while cur != None:
            remains = cur.next
            cur.next = parent
            parent = cur
            cur = remains
        
        return parent