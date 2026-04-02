class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        # push first k elements onto the heap
        for i in range(k):
            heapq.heappush(heap, nums[i])

        # for any remaining numbers, pop the top of the heap (smallest)
        # if the current number is greater than it
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        # maintained heap order ensures that the top of the heap is the
        # smallest of the k largest elements in the array, making it
        # the kth largest element
        return heap[0]