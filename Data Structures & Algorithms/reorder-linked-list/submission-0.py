# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return

        # slow pointer lands at midpoint of list, and fast pointer lands
        # at end of list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # now we need to reverse the second half of the list
        prev = None
        # second half of the list starts at the node after the midpoint
        curr = slow.next
        # disconnect the two halves of the list
        slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # now the prev pointer points to the start of the reversed
        # half of the list
        # head points to the start of the list
        left, right = head, prev
        while right:
            # store the next left and next right in temp vars since both
            # halves of the list are disconnected
            temp1 = left.next
            temp2 = right.next
            # left points to right, and then right points to the next left
            left.next = right
            right.next = temp1
            # left and right pointers are incremented to the next ones, as
            # stored by the temp variables
            left = temp1
            right = temp2