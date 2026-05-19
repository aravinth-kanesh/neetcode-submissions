# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        heapq.heapify(heap)

        count = 0
        for lst in lists:
            if lst:
                heap_node = (lst.val, count, lst)
                heapq.heappush(heap, heap_node)
                count += 1

        dummy = ListNode()
        cur = dummy
        
        while heap:
            val, count, lst = heapq.heappop(heap)

            cur.next = lst
            
            cur = cur.next
            lst = lst.next

            if lst:
                heap_node = (lst.val, count, lst)
                heapq.heappush(heap, heap_node)

        return dummy.next
