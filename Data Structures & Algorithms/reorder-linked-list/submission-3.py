# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # split the list after slow pointer

        head2 = slow.next
        slow.next, prev = None, None

        while head2:
            temp = head2.next
            head2.next = prev
            prev = head2
            head2 = temp

        # prev now points to the reversed head

        head2 = prev

        # now reorder the lists - list and reversed list have been split

        while head2:
            temp1 = head.next
            temp2 = head2.next

            head.next = head2
            head2.next = temp1

            head = temp1
            head2 = temp2