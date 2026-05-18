# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        # start before the linked list
        slow = fast = dummy

        # move the fast pointer n steps
        for _ in range(n):
            # do not need to worry about invalid state where fast
            # reaches the end of the list
            fast = fast.next

        # stop when fast pointer reaches the end of the linked list
        while fast and fast.next:
            # move both pointers one step at a time
            slow = slow.next
            fast = fast.next

        # now slow pointer is one step before the one to remove

        # remove the node after the slow pointer
        slow.next = slow.next.next

        return dummy.next


