# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        r_head = slow.next
        slow.next = None
        prev = None
        while r_head:
            temp = r_head.next
            r_head.next = prev
            prev = r_head
            r_head = temp
        r_head = prev

        dummy = ListNode(next=head)
        while r_head:
            temp1 = head.next
            temp2 = r_head.next
            head.next = r_head
            r_head.next = temp1
            head = temp1
            r_head = temp2