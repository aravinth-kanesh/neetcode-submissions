class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return None

        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if heap and num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        return heap[0]