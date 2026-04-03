# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # the intuition behind this problem is to advance a fast pointer
        # n steps, and then move the slow and fast pointer simultaneously
        # until fast reaches the end of the linked list. At this point,
        # the element at slow.next is the element to remove

        # initialise a dummy pointer and set dummy.next to head
        dummy = ListNode(0, head)

        # point slow and fast to the dummy pointer (before the 1st elem)
        slow = fast = dummy

        # n is always less than the number of nodes - do not need to
        # check for edge of n > number of nodes
        # advance the fast pointer n steps
        for _ in range(n):
            # this operation will not take the code into an invalid state
            fast = fast.next

        # fast pointer must stop at the end of the linked list, so must
        # loop while fast.next is not None
        while fast.next:
            slow = slow.next
            fast = fast.next

        # now slow pointer is one behind the element to remove
        # remove the node
        slow.next = slow.next.next

        # dummy.next points to the start of the list
        return dummy.next