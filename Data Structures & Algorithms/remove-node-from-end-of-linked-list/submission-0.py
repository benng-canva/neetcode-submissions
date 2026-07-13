# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        for i in range(n):
            fast = fast.next
        
        prev, slow = ListNode(), head
        dummy = prev
        prev.next = slow
        while fast != None:
            prev = slow
            slow = slow.next
            fast = fast.next

        prev.next = slow.next

        return dummy.next