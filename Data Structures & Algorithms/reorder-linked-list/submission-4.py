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

        # split the list from slow.next onwards
        r_head = slow.next
        slow.next = None

        # reverse 2nd list
        prev = None
        while r_head:
            temp = r_head.next
            r_head.next = prev
            prev = r_head
            r_head = temp

        # prev now points to head of reversed list
        r_head = prev

        dummy = ListNode(next=head)

        # non-reversed list will always have same or more nodes than the
        # reversed list
        while r_head:
            # save both next pointers
            temp1 = head.next
            temp2 = r_head.next

            # reorder
            head.next = r_head
            r_head.next = temp1

            # increment both head pointers
            head = temp1
            r_head = temp2