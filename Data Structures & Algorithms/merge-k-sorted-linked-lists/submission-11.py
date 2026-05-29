# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [] # min heap
        count = 0

        for lst in lists:
            # check list is not None
            if lst:
                heapq.heappush(heap, (lst.val, count, lst))
                count += 1 # to break value ties in the heap

        dummy = head = ListNode()

        while heap:
            val, count, lst = heapq.heappop(heap)
            head.next = lst # still points to the current value
            head = head.next

            if lst.next:
                # add next node from current list
                heapq.heappush(heap, (lst.next.val, count, lst.next)) 

        return dummy.next