# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            # store next element safely
            temp = head.next

            # make head point to prev
            head.next = prev

            # increment prev and next
            prev = head
            head = temp

        # after, prev will be head of new list
        return prev

        # time is O(n) and space is O(1)