# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p2 = p3 = head
        size = 0

        while head:
            size += 1
            head = head.next

        if n == size:
            return p3.next

        for i in range(size - n - 1):
            p2 = p2.next

        p2.next = p2.next.next
        return p3