# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return True

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next

        if fast:
            slow = slow.next
        
        to_reverse = head
        while to_reverse.next is not slow:
            to_reverse = to_reverse.next
        
        reverse_head = to_reverse.next
        to_reverse.next = None

        temp = reverse_head
        prev = None
        front = None
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        
        reverse_head = prev

        cur1 = head
        cur2 = reverse_head

        while cur2:
            if cur1.val != cur2.val:
                return False
            cur1 = cur1.next
            cur2 = cur2.next

        return True 
        

        
        
        