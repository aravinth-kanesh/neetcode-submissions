# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            # slow moves one step at a time, fast moves two
            slow = slow.next
            fast = fast.next.next

            # cycle detected
            if slow == fast:
                return True

        return False