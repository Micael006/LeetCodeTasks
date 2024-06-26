# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        extra = 0
        cur_l = l1
        cur_r = l2
        while cur_l.next is not None:
            cur_val = cur_l.val + extra

            if cur_r is not None:
                cur_val += cur_r.val
                cur_r = cur_r.next
            
            cur_l.val = cur_val % 10
            extra = cur_val // 10
            cur_l = cur_l.next

        cur_val = cur_l.val + extra
        if cur_r is not None:
            cur_val += cur_r.val
            cur_r = cur_r.next

        cur_l.val = cur_val % 10
        extra = cur_val // 10
        
        while cur_r is not None:
            cur_val = cur_r.val + extra
            extra = cur_val // 10
            cur_l.next = ListNode(cur_val % 10, None)
            
            cur_l = cur_l.next
            cur_r = cur_r.next
        
        if extra > 0:
            cur_l.next = ListNode(extra, None)
        
        return l1
