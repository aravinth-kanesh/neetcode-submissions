# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        cur = dummy

        # iterate through both linked lists simulataneously
        while l1 and l2:
            total = l1.val + l2.val + carry
            value, carry = total % 10, total // 10
            print(value)
            cur.next = ListNode(value)
            l1, l2, cur = l1.next, l2.next, cur.next

        # numbers can be different lengths
        while l1:
            total = l1.val + carry
            value, carry = total % 10, total // 10
            cur.next = ListNode(value)
            l1, cur = l1.next, cur.next

        while l2:
            total = l2.val + carry
            value, carry = total % 10, total // 10
            cur.next = ListNode(value)
            l2, cur = l2.next, cur.next

        if carry:
            cur.next = ListNode(carry)
        
        return dummy.next
