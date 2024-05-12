# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        left = l1
        right = l2
        overflow = 0
        while left.next is not None and right.next is not None:
            cur_val = left.val + right.val + overflow
            left.val, overflow = cur_val % 10, cur_val // 10
            left = left.next
            right = right.next
        cur_val = left.val + right.val + overflow
        left.val, overflow = cur_val % 10, cur_val // 10
        if left.next is None and right.next is None:
            if overflow != 0:
                left.next = ListNode(overflow, None)
            return l1
        if right.next is None:
            left = left.next
        else:
            left.next = right.next
            left = left.next

        while overflow > 0 and left.next is not None:
            cur_val = left.val + overflow
            left.val, overflow = cur_val % 10, cur_val // 10
            left = left.next
        cur_val = left.val + overflow
        left.val, overflow = cur_val % 10, cur_val // 10
        if overflow > 0:
            left.next = ListNode(overflow, None)
        return l1
             


