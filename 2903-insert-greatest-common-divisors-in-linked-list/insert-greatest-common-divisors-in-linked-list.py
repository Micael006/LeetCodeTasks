# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur.next:
            temp = cur.next
            new_node = ListNode(math.gcd(cur.val, temp.val), temp)
            cur.next = new_node
            cur = cur.next
            cur = cur.next
        return head