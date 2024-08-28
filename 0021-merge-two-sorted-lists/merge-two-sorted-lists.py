# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode(-1)
        cur = answer
        left = list1
        right = list2

        while left or right:
            if left and right:
                if left.val <= right.val:
                    cur.next = left
                    left = left.next
                else:
                    cur.next = right
                    right = right.next
            elif left:
                cur.next = left
                left = None
            else:
                cur.next = right
                right = None
            cur = cur.next
        
        return answer.next
        