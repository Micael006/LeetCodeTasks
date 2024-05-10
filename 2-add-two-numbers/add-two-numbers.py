# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next
    
    def add(self, val):
        cur = self.val
        if cur == -1:
            self.val = val
            return
        cur = self
        while cur.next is not None:
            cur = cur.next
        cur.next = ListNode(val)
        return

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur_left = l1
        cur_right = l2
        buffer = 0
        result = ListNode()
        empty = True
        while cur_left is not None or cur_right is not None:
            if cur_left is not None:
                buffer += cur_left.val
            if cur_right is not None:
                buffer += cur_right.val
            if not empty:
                result.add(buffer % 10)
            else:
                result.val = buffer % 10
                empty = False
            buffer //= 10
            if cur_left is not None:
                cur_left = cur_left.next
            if cur_right is not None:
                cur_right = cur_right.next
        if buffer > 0:
            if empty:
                result.val = buffer
                empty = False
            else:
                result.add(buffer)
        return result