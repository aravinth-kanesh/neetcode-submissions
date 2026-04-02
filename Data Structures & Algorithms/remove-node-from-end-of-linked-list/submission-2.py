# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy

        # move the fast pointer ahead of the slow one by n placed
        for _ in range(n):
            fast = fast.next

        # move both pointers until the fast pointer reaches the end of the list
        # by this point, the slow pointer will be just before the node to delete
        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next

        

