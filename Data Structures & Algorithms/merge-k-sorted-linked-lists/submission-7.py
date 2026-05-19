# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # add first node from each list to a max heap
        heap = []
        heapq.heapify(heap)
        
        count = 0

        for lst in lists:
            # list may be empty
            if lst:
                # will order by value first, then count
                heap_node = (lst.val, count, lst)
                heapq.heappush(heap, heap_node)

                # increment count
                count += 1

        # create new result linked list
        dummy = ListNode()
        cur = dummy

        # keep iterating while there are nodes left to add
        while heap:
            val, count, lst = heapq.heappop(heap)

            # only need the list for now
            cur.next = lst

            # move the pointers along
            cur = cur.next
            lst = lst.next

            # add the list back to the heap if there are still
            # nodes left
            if lst:
                heap_node = (lst.val, count, lst)
                heapq.heappush(heap, heap_node)

        # return head of sorted ll
        return dummy.next
