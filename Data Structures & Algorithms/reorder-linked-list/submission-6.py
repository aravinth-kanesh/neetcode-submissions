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

        # node after slow is the first node in the reversed list (last)
        r_head = slow.next

        # disconnect the two lists
        slow.next = None

        # reverse the list
        prev = None
        while r_head:
            temp = r_head.next
            r_head.next = prev
            prev = r_head
            r_head = temp

        # prev now points to head of reversed list
        r_head = prev

        # reorder the list now (reversed list is always same length of shorter)
        while r_head:
            temp1 = head.next
            temp2 = r_head.next

            head.next = r_head
            r_head.next = temp1

            head = temp1
            r_head = temp2        