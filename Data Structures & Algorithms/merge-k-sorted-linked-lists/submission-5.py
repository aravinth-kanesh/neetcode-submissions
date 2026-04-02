# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # we use a heap which holds at most k elements, where k is the
        # number of lists 
        heap = []

        # push smallest element from each list to the heap
        # include index to break ties when values are the same
        for i, node in enumerate(lists):
            # if we haven't reached the end of the list
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        cur = dummy

        while heap:
            # pop the smallest element from the heap
            val, i, node = heapq.heappop(heap)
            
            # add it to the linked list
            cur.next = node
            cur = cur.next

            # push the next element of the smallest if it isn't None
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next

            