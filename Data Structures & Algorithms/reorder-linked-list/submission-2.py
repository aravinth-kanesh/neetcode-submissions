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
        
        # slow.next is the end of the reversed list now
        reversed_head = slow.next

        # split the list
        slow.next = None

        # reverse the second half of the list
        prev = None
        
        while reversed_head:
            temp = reversed_head.next
            reversed_head.next = prev
            prev = reversed_head
            reversed_head = temp

        # second half is reversed now and prev points to the start
        # of the reversed list

        # point reversed_head to real head
        reversed_head = prev

        # reorder the list
        while reversed_head:
            temp1 = head.next
            temp2 = reversed_head.next

            head.next = reversed_head
            reversed_head.next = temp1

            head = temp1
            reversed_head = temp2


            

        


