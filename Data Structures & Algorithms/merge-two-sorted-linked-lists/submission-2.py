# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create result linked list
        # dummy needed to point to head of the new list at the end
        dummy = ListNode()
        cur = dummy

        # both linked lists can be empty - edge case
        if not list1 and not list2:
            return None

        # make sure to advance the respective pointers
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next

            # don't forget to advance cur as well
            cur = cur.next

        if list1:
            cur.next = list1
        if list2:
            cur.next = list2

        return dummy.next

    
        