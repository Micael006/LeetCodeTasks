# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverse_linked_list(linked_list):
            cur_node = linked_list
            prev_node = None
            next_node = None
            while cur_node:
                next_node = cur_node.next
                temp = prev_node
                prev_node = cur_node
                prev_node.next = temp

                cur_node = next_node
            
            return prev_node
        
        head = reverse_linked_list(head)
        if n == 1:
            head = head.next
        else:
            cur = head
            while n > 2:
                cur = cur.next
                n -= 1
            if cur.next:
                cur.next = cur.next.next
            else:
                cur.next = None
        
        return reverse_linked_list(head)
