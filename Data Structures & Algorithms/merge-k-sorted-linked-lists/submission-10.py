# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        count = 0
        for lst in lists:
            heapq.heappush(heap, (lst.val, count, lst))
            count += 1

        dummy = head = ListNode()

        while heap:
            val, count, lst = heapq.heappop(heap)
            head.next = ListNode(val)
            
            head = head.next
            lst = lst.next

            if lst:
                heapq.heappush(heap, (lst.val, count, lst))

        return dummy.next

