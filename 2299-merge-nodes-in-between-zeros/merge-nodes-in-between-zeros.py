# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last_head = ListNode(head.val)
        last = last_head
        cur = head.next
        while cur.next is not None:
            if cur.val == 0:
                last.next = ListNode(0, None)
                last = last.next
            else:
                last.val += cur.val
            cur = cur.next
        return last_head