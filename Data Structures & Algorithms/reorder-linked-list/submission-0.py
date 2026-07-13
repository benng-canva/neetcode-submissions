# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        slow.next = None

        even, odd = head, self.reverse(mid)
        while even != None and odd != None:
            tmp1, tmp2 = even.next, odd.next
            even.next = odd
            odd.next = tmp1
            even, odd = tmp1, tmp2


    def reverse(self, head):
        prev, node = None, head

        while node:
            nextNode = node.next
            node.next = prev
            prev = node
            node = nextNode

        return prev