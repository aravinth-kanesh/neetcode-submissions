# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # the key to solving this problem is definitely that each
        # linked list is sorted. Finding the minimum value at each
        # iteration would make this an efficient solution, as the 
        # required time complexity is O(n * k) - this means that each
        # linked list node should only be accessed once (or multiples)

        if len(lists) == 0:
            return None

        for i in range(1, len(lists)):
            lists[i] = self.mergeLists(lists[i], lists[i - 1])

        return lists[-1]

    def mergeLists(self, l1, l2):
        dummy = ListNode()
        head = dummy

        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next

            head = head.next

        if l1:
            head.next = l1
        if l2:
            head.next = l2

        return dummy.next

        