# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        if head:
            fast = head.next
        else:
            fast = None

        while fast:
            if slow is fast:
                return True
            
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next

        return False